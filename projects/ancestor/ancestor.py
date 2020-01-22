from util import Stack
from graph import Graph

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.

        If both exist, and a connection from v1 and v2 in self.vertices
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist')

    # def get_neighbors(self, vertex_id):
    #     """
    #     Get all neighbors (edges) of a vertex.
    #     """
    #     return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):

    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])

    queue = Queue()
    queue.enqueue([starting_node])
    max_len = 1
    earliest_ancestor = -1
    while queue.size()> 0:
        path = queue.dequeue()
        voss = path[-1]
        if [len(path) >= max_len and voss < earliest_ancestor or (len(path) > max_len)]:
            earliest_ancestor = voss
            max_len = 1
        for neighbor in graph.vertices[voss]:
            path_copy = list(path)
            path_copy.append(neighbor)
            queue.enqueue(path_copy)
    return earliest_ancestor
    
    # ancestor = starting_node
    # generation = 0
    # stack = push([ancestor, generation])

    # while len(stack) > 0:
    #     (child, childs_gen) = stack.pop()
    #     if childs_gen > generation:
    #         ancestor = child
    #         generation = childs_gen
    #     elif childs_gen == generation and child < ancestor:
    #         ancestor = child
    #     parents = graph.get_neighbors(child)
    #     stack.extend([parent, childs_gen + 1] for parent in parents)

    