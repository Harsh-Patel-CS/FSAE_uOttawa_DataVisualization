# Harsh Patel

import database_options


class database_manager():
    def __init__(self):
        self.databases = {}

    def new_database(self, name, file_path):
        self.databases[name] = database_options.database(name,file_path)

        