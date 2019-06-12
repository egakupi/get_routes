class Graph(object):

    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def find_all_paths(self, start_vertex, end_vertex, path=[], edge_number=3):
        if edge_number >= 0:
            graph = self.__graph_dict
            path = path + [start_vertex]
            if start_vertex == end_vertex:
                return [path]
            if start_vertex not in graph:
                return []
            paths = []
            for vertex in graph[start_vertex]:
                if vertex not in path:
                    extended_paths = self.find_all_paths(vertex,
                                                         end_vertex,
                                                         path, edge_number=edge_number - 1)
                    if extended_paths:
                        for p in extended_paths:
                            paths.append(p)
            return paths
        else:
            return None
