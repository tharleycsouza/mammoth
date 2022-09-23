# Dockerfile

# FROM directive instructing base image to build upon
FROM postgres:10
RUN apt-get update
RUN apt-get install ssh -y
RUN apt-get install rsync -y
#COPY entrypoint.sh /entrypoint.sh
#RUN chmod +x /entrypoint.sh

#ENTRYPOINT ["/entrypoint.sh"]
#RUN mkdir -p /var/lib/postgresql/.ssh
#RUN chmod 700 /var/lib/postgresql/.ssh
#RUN echo archive_mode = on > /var/lib/postgresql/data/postgresql.conf
#RUN echo archive_command = 'rsync -av %p barman@:/var/lib/barman/db/incoming/%f' > /var/lib/postgresql/data/postgresql.conf
#COPY ./postgres /var/lib/postgresql/.ssh
#RUN chmod 700 /var/lib/postgresql/.ssh/postgres
#RUN echo ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDOj9dEHoawhswfsHjhPxpuWxPw1qkouAHTIU0W9sK8EeagiFHqi4D+4sd8XIFAVYh4M3LybYWNz37VwuLrW7kOJNjI9PUU7Nt6lmUCjIqgiqFdNmpEXfF1cFwjlLGwBsMo78NSIpB0UeZnhoT53dCofDTtpN3UgBzupMrzOs9HYNdgwVjZgxAbWRlP4KsMoHP07HxrOysZ8mUFoNCySId9Nn6dIS5qV1E9T7KNlHQmahrN92IrvME3v7wy/MMfWfGxMzoElJ37ePP98xAc9HrU8dXJ7mh1jUyCSwAzopAgsT/X1WejY9byJSWaZo3BO/mksz+lubzA6/xUd+r5scO7 barman@5e7239a0486b > /var/lib/postgresql/.ssh/authorized_keys2
#RUN chmod 600 /var/lib/postgresql/.ssh/authorized_keys2
#RUN chown -R postgres.postgres /var/lib/postgresql/.ssh
#RUN echo  "  IdentityFile /var/lib/postgresql/.ssh/postgres" > /etc/ssh/ssh_config
#RUN mkdir -p /run/sshd
##RUN /lib/systemd/systemd-sysv-install enable ssh
##RUN service ssh start
##RUN service ssh start
#RUN service ssh status

#archive_mode = on       
#archive_command = 'rsync -av %p barman@db:/var/lib/barman/db/incoming/%f'
##