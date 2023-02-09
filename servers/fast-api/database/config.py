import os

TORTOISE_ORM = {
    "connections": {"default": 'sqlite:///{}/app.db'.format(os.path.dirname(__file__))},
    "apps": {
        "models": {
            "models": [
                "database.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}