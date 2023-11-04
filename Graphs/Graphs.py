class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def bfs(self, node):
        visited = []
        queue = []
        visited.append(node)
        queue.append(node)

        while queue:
            i = queue.pop(0)
            print(i, end=" ")

            for neighbor in self.adjacency_list[i]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)


    def dfs(self, node):
        visited = [node]
        stack = [node]
        while stack:
            pop_vertex = stack.pop()
            print(pop_vertex)
            for neighbor in self.adjacency_list[pop_vertex]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    stack.append(neighbor)



graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")
print(graph.add_edge("A","B"))
print(graph.add_edge("A","C"))
print(graph.add_edge("B","D"))
print(graph.add_edge("D","E"))
print(graph.add_edge("D","F"))
print(graph.add_edge("C","E"))
print(graph.add_edge("E","F"))

graph.print_graph()
graph.dfs("A")


customDict = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
               }


