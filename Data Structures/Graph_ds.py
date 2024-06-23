class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dict:", self.graph_dict)

    def get_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_path(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path

if __name__ == "__main__":
    routes = [
        ("Tehran", "Dubai"),
        ("Tehran", "Rome"),
        ("Dubai", "Rome"),
        ("Dubai", "Torento"),
        ("Rome", "Torento"),
        ("Torento", "New York")
    ]

    route_graph = Graph(routes)

    print("_____________________________________________")
    print("Tehran to Tehran:")
    start = "Tehran"
    end = "Tehran"
    print(f"path between {start} and {end}:", route_graph.get_path(start, end))
    print("_____________________________________________")
    print("Torento to Tehran(We dont heve flight):")
    start = "Torento"
    end = "Tehran"
    print(f"path between {start} and {end}:", route_graph.get_path(start, end))
    print("_____________________________________________")
    print("Tehran to Torento:")
    start = "Tehran"
    end = "Torento"
    print(f"path between {start} and {end}:", route_graph.get_path(start, end))
    print("_____________________________________________")
    print("Shortest path from Tehran to Torento:")
    start = "Tehran"
    end = "Torento"
    print(f"shortest path between {start} to {end}:", route_graph.get_shortest_path(start, end))