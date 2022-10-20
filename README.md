# Django + MongoDB
---
## MongoDB settings
Create an ```.env``` file in ```django_mongo/djangomongo``` directory:
```
MONGODB_CONNECTION=mongodb
MONGODB_HOST=127.0.0.1
MONGODB_PORT=27017
MONGODB_USERNAME=
MONGODB_PASSWORD=

MONGODB_DBNAME="your database name"
MONGODB_CONFIG_COLLECTION_NAME="your config collection name"
```

## Project settings
### Virtual environment
Run ```python -m venv venv``` to create a virtual environment.

Then ```source ./venv/bin/activate``` (on MacOS) or ```venv\Scripts\activate``` (on Windows) to activate the virtual environment.
### Python packages
Run ```pip install -r requirements.txt``` to install required packages.
### Run server
Execute ```python manage.py runserver```.

The server should be running at ```127.0.0.1:8000/```

## APIs
### Get all configs
<b>GET</b>  ```127.0.0.1:8000/configs/```

### Add new config
<b>POST</b> ```127.0.0.1:8000/configs/```

The POST body should look like this:
```
{
    "name": "New config",
    "description": "Some description",
    "url": "example.com",
    "attributes": [
        {
            "name": "Product name",
            "value": "Some XPath value of product name"
        },
        {
            "name": "Product price",
            "value": "Some XPath value of product price"
        }
    ]
}
```
