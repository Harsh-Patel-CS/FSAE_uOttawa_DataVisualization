#Harsh Patel

import dearpygui.dearpygui as dpg

class graph():
    def __init__(self, name, database, graph_type):
        self.name=name
        self.databases = [database]
        self.type = graph_type
        with dpg.window(tag=name):
            pass


    def add_database(self,database):
        self.databases.append(database)
        print(self.databases)







    