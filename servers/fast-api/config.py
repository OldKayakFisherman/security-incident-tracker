import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    def __init__(self):
        self._database_url = "sqlite:///./app.sqlite?cache=shared"
        self._secret_key = os.getenv('SECRET_KEY')
        self._algorithm = os.getenv('ALGORITHM')
        self._token_expires = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
        self._default_admin_username = os.getenv('DEFAULT.ADMIN.USER')
        self._default_admin_password = os.getenv('DEFAULT.ADMIN.PASSWORD')
        self._default_normy_username = os.getenv('DEFAULT.NORMY.USER')
        self._default_normy_password = os.getenv('DEFAULT.NORMY.PASSWORD')

    def get_secret_key(self):
        return self._secret_key

    def get_algorithm(self):
        return self._algorithm

    def get_token_expires(self):
        return self._token_expires

    def get_default_admin_username(self):
        return  self._default_admin_username

    def get_default_admin_password(self):
        return  self._default_admin_password

    def get_default_normy_username(self):
        return self._default_normy_username

    def get_default_normy_password(self):
        return self._default_normy_password

    def get_database_url(self):
        return self._database_url
