import random


# represents each word object/vertex/word point/node
class Vertex:
    # initiation of a vertex and creation of a dictionary to store adjacent nodes
    def __init__(self, value):
        self.value = value  # the word itself
        self.adjacent = {}  # to store each adjacent(has an edge) word/node as key and the edge's
        # (connection) weight as a value
        self.neighbours = []  # stores the adjacent words (keys)
        self.neighbour_weights = []  # stores the adjacent word weights (values)

    # method to add edges
    def add_edge_to(self, vertex, weight=0):
        # connects the vertex to an adjacent vertex
        self.adjacent[vertex] = weight

    # method to increase the weight of edges
    def increment_edge(self, vertex):
        # if a node goes to adjacent vertex we want to increase weight of connection
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1  # if already present get value else create then add 1

    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbours.append(vertex)
            self.neighbour_weights.append(weight)

    """ method to randomly select the next word from adjacent words based on edge weights.
    To be able to do this we also create a probability mapp above, where we store each
    vertex in a list and its weight in another list. So the random choice method will
    randomly select a vertex object from the vertex list based on weights in the weights list.
    As I understand, we can directly pass these as keys and values lists without
    using the method above, but will be less readable"""

    def next_word(self):
        return random.choices(self.neighbours, weights=self.neighbour_weights)[0]  # get the first word in the list


# the graph constructed from the vertex objects
class Graph:
    # initializes a dictionary where word strings (keys) are mapped to vertices (vertex objects)
    def __init__(self):
        self.vertices = {}  # will be used to store the created vertices and looking them up

    # method to get all the possible words (vertex values)
    def get_vertex_values(self):
        return set(self.vertices.keys())

    # method to add new words to the graph
    def add_vertex(self, value):
        # create the vertex for the given value (word) and add it to the vertices dictionary
        self.vertices[value] = Vertex(value)

    # method to obtain the mapped vertex object for a certain word value
    # also creates a vertex if word is not in collection
    def get_vertex(self, value):
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]

    # method to get the next word randomly but based on edge weight
    # for this we add a next_word method to the Vertex class as well, and we'll pass its result here
    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    # method to get probability mappings for each vertex in graph
    # will be used for the generation of the graph based on probability maps of nodes
    def generate_probability_mappings(self):
        for vertex in self.vertices.values():  # values because you need the vertex object
            vertex.get_probability_map()
