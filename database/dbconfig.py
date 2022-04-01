import os
from configparser import ConfigParser


# getting path for database.ini file
def _get_file_path(filename):
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, filename)


# loading and returning config parameters for database
def config(filename=_get_file_path('database.ini'), section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db
