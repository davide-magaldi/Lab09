import networkx as nx

from database.DAO import Dao
from model.connection import Connection


class Model:
    def __init__(self):
        self.airports = {}
        self.getAllAirports()
        self.connections = []
        self.getConnections()
        self._graph = nx.Graph()

    def getAllAirports(self):
        airports = Dao.getAllAirports()
        for a in airports:
            self.airports[a.ID] = a

    def getConnections(self):
        all_connections = Dao.getAllConnections()
        for r in all_connections:
            presente = False
            for c in self.connections:
                if r["origin_airport_id"] == c.destination_airport_id and r["destination_airport_id"] == c.origin_airport_id:
                    c.updateConnection(r["distance"], r["count"])
                    presente = True
                    break
            if not presente:
                connection = Connection(**r)
                self.connections.append(connection)

    def buildGraph(self, distance):
        self._graph.clear()
        self._graph.add_nodes_from(self.airports.values())
        self.addEdges(distance)

    def addEdges(self, distance):
        for c in self.connections:
            if c.distance > distance:
                self._graph.add_edge(self.airports[c.origin_airport_id], self.airports[c.destination_airport_id], weight=c.distance)

    def getNumNodi(self):
        return len(self._graph.nodes)

    def getNumArchi(self):
        return len(self._graph.edges)

    def getEdges(self):
        return self._graph.edges


