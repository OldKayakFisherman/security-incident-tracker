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


class DatabaseUtilities:

    def __init__(self, dsn):
        self._dsn = dsn

    def does_table_exist(self, table) -> bool:

        qr = QueryReader()
        sql = qr.get_table_check_statement()

        with connect(self._dsn) as cn:
            eval_record = cn.execute_scalar(sql, param={"tablename": table})

        return eval_record

    def ensure_created(self):

        sr = SchemaReader()

        if not self.does_table_exist("users"):
            with connect(self._dsn) as cn:
                cn.execute(sr.get_user_table_statement())

        if not self.does_table_exist("incidents"):
            with connect(self._dsn) as cn:
                cn.execute(sr.get_incident_table_statement())


class UserRepository:

    def __init__(self, dsn):
        self._dsn = dsn
        self._user_insert = QueryReader().get_user_insert_statement()
        self._user_by_email = QueryReader().get_user_by_email_statement()

    def getUser(self, email: str):
        null_eval = None
        with connect(self._dsn) as cn:
            user = cn.query_first_or_default(self._user_by_email,
                                                   model=UserEntity,
                                                   default=null_eval,
                                                   param={"email": email}
                                                   )
        if null_eval is None:
            return user
        else:
            return null_eval

    def add_user(self, user: UserEntity):

        with connect(self._dsn) as cn:
            cn.execute(self._user_insert,
                             param=[{"email": user.email, "password": user.password,
                                    "is_active": user.is_active, "is_admin":user.is_admin}])


