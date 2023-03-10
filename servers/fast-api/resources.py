import os


def read_schema_resource():

    retval = None

    current_dir = os.path.dirname(os.path.realpath(__file__))
    target_path = os.path.join(current_dir, 'scripts', 'schema', 'schema.sql')

    with open(target_path, "r+") as schema_file:
        retval = schema_file.read()

    return retval


class SchemaReader:
    def __init__(self):
        self._current_dir = os.path.dirname(os.path.realpath(__file__))

    def get_schema_statements(self):

        target_path = os.path.join(self._current_dir, 'scripts', 'schema', 'schema.sql')

        with open(target_path, "r+") as schema_file:
            retval = schema_file.read()

        return retval.split(';')


class QueryReader:

    def __init__(self):
        self._current_dir = os.path.dirname(os.path.realpath(__file__))

    def get_user_insert_statement(self):
        return self._read_query('qry_insert_users')

    def get_user_by_email_statement(self):
        return self._read_query('qry_retrieve_user_by_email')

    def _read_query(self, query):

        target_path = os.path.join(self._current_dir, 'scripts', 'queries', query)

        with open(target_path, "r+") as schema_file:
            return schema_file.read()

