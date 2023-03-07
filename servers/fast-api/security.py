from datetime import timedelta, datetime

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from config import Settings

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
