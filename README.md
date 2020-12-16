# Mammoth

Admin for creating and management the barman server and pg_server

## Installation

Use the package manager [pip](https://github.com/tharleycsouza/mammoth.git) to install mammoth.

```bash
pip install git+https://github.com/tharleycsouza/mammoth.git
```

## Usage

Project with docker-compose 

- docker-compose up -d --build
- docker-compose exec web python manage.py makemigrations
- docker-compose exec web python manage.py migrate
- docker-compose exec web python manage.py createsuperuser



```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)