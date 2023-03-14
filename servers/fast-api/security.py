from datetime import timedelta, datetime

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from config import Settings
from db import UserRepository


class Token:
    access_token: str
    token_type: str


class SystemUser:
    username: str
    role: str


class AuthenticationUtility:

    def __int__(self, dsn):
        self._user_repository = UserRepository(dsn)
        self._pu = PasswordUtility()

    def authenticate_user(self, username, password) -> SystemUser:

        retval = None
        user_entity = self._user_repository.getUser(username)

        if user_entity is not None:
            retval = SystemUser()
            retval.username = user_entity.email
            retval.role = "normy" if user_entity.is_admin else "admin"
        return retval


class PasswordUtility:

    def __init__(self):
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, hashed_password):
        return self._pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self._pwd_context.hash(password)



class TokenUtility:

    def __init__(self):
        self._oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
        self._config = Settings()

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self._config.get_secret_key(), algorithm=self._config.get_algorithm())
        return encoded_jwt
