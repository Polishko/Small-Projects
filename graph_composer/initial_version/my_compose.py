import random
import string
from my_graph import Graph


# the function to read a text file and get the words from it in a simplified format
def get_words_from_text(text_path):
    """we remove all whitespaces (make them space), then
         convert everything to lowercase and finally remove punctuation marks to simplify things"""
    with open(text_path, "r") as f:  # we open the file as f to read it
        text = f.read()  # store read info in text variable
        text = " ".join(text.split()).lower().translate(str.maketrans("", "", string.punctuation))

    # get a list of words
    return text.split()


# the function that will make the graph itself
def make_graph(words):
    g = Graph()  # here we create the graph object

    previous = None  # this is the word before the current which is none for the first word

    for word in words:
        word_vertex = g.get_vertex(word)  # so here we get the vertex if it exists, if not we create it
        # then we want to increase weight of connection between the vertex if there is a previous adjacent one
        if previous:
            previous.increment_edge(word_vertex)  # keeping track of the weight eliminates
            # the need to count occurrence of word
        previous = word_vertex  # we set the current as the previous and prepare it for the next word in the list

    # so we have created our vertex objects and their edges now we can create the mappings

    g.generate_probability_mappings()  # this will generate a probability map for each vertex in the g object
    # therefore it will populate the neighbour and neighbour weight lists for each vertex

    return g  # we return the final graph


# the function that will get next word randomly and compose a new text for a given length
def compose(g, words, length=100):
    composition = []  # the text that we'll compose
    word = g.get_vertex(random.choice(words))  # we get the vertex obj of a word randomly selected from the words list
    # make the composition based on given length
    for _ in range(length):
        composition.append(word.value)  # we append the string to the composition
        word = g.get_next_word(word)  # here we get a next adjacent word object
        # randomly but based on neighbours weight

    return composition


# the function that combines all the construction steps
def main():
    # 1. we get all the words from the given text file in the form of a list
    words = get_words_from_text("texts/hp_sorcerer_stone.txt")
    # 2. we create our graph object with all vertexes and their relations
    g = make_graph(words)
    # 3. we want to construct the words
    composition = compose(g, words, 100)  # 100 is th selected length, can be something else

    return " ".join(composition)  # return the composition in the form of string


if __name__ == "__main__":
    print(main())
