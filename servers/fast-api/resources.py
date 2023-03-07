import os


def read_schema_resource():

    retval = None

    current_dir = os.path.dirname(os.path.realpath(__file__))
    target_path = os.path.join(current_dir, 'scripts', 'schema.sql')

    print(target_path)

    with open(target_path, "r+") as schema_file:
        retval = schema_file.read()

    return retval
