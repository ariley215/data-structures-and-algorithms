from .queue import Queue
class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        self.adjacency = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self.adjacency[vertex] = [] # add vertex to dictionary

        return vertex

    def size(self):
        return len(self.adjacency) # when a dictionary is in len it returns the number of keys

    def add_edge(self, start_vertex, end_vertex, weight=None):
        if start_vertex or end_vertex not in self.adjacency:
            raise KeyError("both vertices must be in the graph")
        edge = Edge(end_vertex, weight) # create new edge
        # add edge to the starting vertex's neighbors list in the adjacency_list
        self.adjacency[start_vertex].append(edge)

    def get_neighbors(self, vertex):
        pass

    def get_nodes(self):
        pass

    def breadth_first(self, first_node):
        visited = set()
        queue = Queue()
        queue.enqueue(first_node)
        while not queue.is_empty():
            dequeued_node = queue.dequeue()
            if dequeued_node in visited:
                continue
            else:
                visited.append(dequeued_node)
                print(dequeued_node)
            for neighbor in dequeued_node.neighbors:
                if neighbor not in visited:
                    queue.enqueue(neighbor)


class Vertex:
   def __init__(self, value):
         self.value = value


class Edge:
   def __init__(self, vertex, weight=None):
       self.vertex = vertex
       self.weight = weight
