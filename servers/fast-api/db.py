import os

from pydapper import connect
from resources import SchemaReader, QueryReader
from config import Settings
from entities import UserEntity, IncidentEntity
from security import PasswordUtility


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

                # Create the default users
                settings = Settings()
                pu = PasswordUtility()
                ur = UserRepository(self._dsn)

                admin_email = settings.get_default_admin_username()
                admin_password = pu.get_password_hash(settings.get_default_admin_password())
                default_admin = UserEntity(None, admin_email, admin_password, True, True)

                ur.add_user(default_admin)

                normy_email = settings.get_default_normy_username()
                normy_password = pu.get_password_hash(settings.get_default_normy_password())

                default_normie = UserEntity(None, normy_email, normy_password, True, False)

                ur.add_user(default_normie)

        if not self.does_table_exist("incidents"):
            with connect(self._dsn) as cn:
                cn.execute(sr.get_incident_table_statement())

    def ensure_destroyed(self, database_name):
        with connect(self._dsn) as cn:
            if self.does_table_exist('incidents'):
                cn.execute("drop table incidents")

            if self.does_table_exist('users'):
                cn.execute("drop table users")

            os.remove(database_name)

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


