import sqlite3
from dataclasses import dataclass
from pydapper import connect
from resources import SchemaReader, QueryReader

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

    def __init__(self, dsn):
        self._dsn = dsn
        self._user_insert = QueryReader().get_user_insert_statement()
        self._user_by_email = QueryReader().get_user_by_email_statement()

    def getUser(self, email: str):
        null_eval = None
        with connect(self._dsn) as commands:
            user = commands.query_first_or_default(self._user_by_email,
                                                   model=UserEntity,
                                                   default=null_eval,
                                                   param={"email": email}
                                                   )
        if null_eval is None:
            return user
        else:
            return null_eval

    def add_user(self, user: UserEntity):

        with connect(self._dsn) as commands:

            commands.execute(self._user_insert,
                             param=[{"email": user.email, "password": user.password,
                                    "is_active": user.is_active, "is_admin":user.is_admin}])


