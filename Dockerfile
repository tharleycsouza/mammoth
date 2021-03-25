FROM python:3.6.9-jessie
RUN apt-get update
RUN apt-get install -y wget cron 

RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" > /etc/apt/sources.list.d/pgdg.list' && \
	wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
	apt-get update && apt-get install -y postgresql-client barman python3-pip python-pip

RUN pip install prometheus_client

# grab gosu for easy step-down from root
ENV GOSU_VERSION 1.7
RUN set -x \
	&& wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
	&& wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
	&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
	&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu \
	&& gosu nobody true


ENV DOCKERIZE_VERSION v0.5.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

#RUN apt-get purge -y python-pip wget && apt-get clean && rm -rf /var/lib/apt/lists/* /var/tmp/*

VOLUME /etc/barman.d/
VOLUME /var/lib/barman/

ENV BARMAN_LOG_FILE=/var/log/barman.log \
	BARMAN_BARMAN_HOME=/var/lib/barman \
	BARMAN_BARMAN_LOCK_DIRECTORY=/tmp \
	BARMAN_CONFIGURATION_FILES_DIRECTORY=/etc/barman.d \
	BARMAN_PRE_BACKUP_SCRIPT=/opt/barman/scripts/pre_backup.sh \
	BARMAN_POST_BACKUP_SCRIPT=/opt/barman/scripts/post_backup.sh \
	PROM_EXPORTER_LOG_FILE="/var/log/barman_prom_exporter.log"

COPY scripts /opt/barman/scripts
COPY docker-entrypoint.sh /

WORKDIR $BARMAN_BARMAN_HOME

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["barman"]
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/mammoth
#RUN pip3 install --upgrade pip3
RUN pip3 install pipenv
RUN apt-get update; apt-get install locales
COPY ./Pipfile /usr/src/mammoth/Pipfile
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
	locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN python3.6 -m pipenv install --skip-lock --system --dev
COPY ./app/local_settings_dev.py /etc/mammoth/local_settings.py