import sqlite3
from dataclasses import dataclass
from pydapper import connect

@dataclass
class UserEntity:
    id: int
    email: str
    password: str
    is_active: bool
    is_admin: bool


@dataclass
class IncidentEntity:
    id: int
    external_case_number: str
    ip: str
    pen_tester: bool
    region: str
    country: str
    description: str
    script_injection: bool
    command_injection: bool
    sql_injection: bool
    cross_frame_scripting: bool
    path_discovery: bool
    cross_site_request_forgery: bool
    other: bool


class UserRepository:

    def __int__(self, dsn):
        self._dsn = dsn;

    def getUser(self, email: str):
        null_eval = None
        with connect(self._dsn) as commands:
            user = commands.query_first_or_default("select * from users where email = '?email?'",
                                                   model=UserEntity,
                                                   default=null_eval,
                                                   param=[email]
                                                   )

        if null_eval is None:
            return user
        else:
            return null_eval

    def add_user(self, user: UserEntity):

        with connect(self._dsn) as commands:

            commands.execute("""
                INSERT INTO users
                (email, password, is_active, is_admin)
            """, param=[user.email, user.password, user.is_active, user.is_admin])


