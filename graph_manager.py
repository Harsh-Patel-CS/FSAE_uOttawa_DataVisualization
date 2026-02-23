# Harsh Patel
import graph_options


class graph_manager():
    def __init__(self):
        self.graphs = {}

    def new_graph(self, name, database, graph_type):
        self.graphs[name] = graph_options.graph(name, database, graph_type)

    def add_database(self, name, database):
        self.graphs[name].add_database(database)


