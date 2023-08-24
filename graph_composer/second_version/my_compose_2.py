# explanation added for new code snippets
# more explanation available in the initial version files
import random
import string
import re
import os
from my_graph_2 import Graph


def get_words_from_text(text_path):
    with open(text_path, "rb") as f:
        text = f.read().decode("utf-8")
        # for song texts we remove text in brackets such as: [choir], [verse] etc
        text = re.sub(r"\[([^\]]+)\]", " ", text)

        text = " ".join(text.split()).lower().translate(str.maketrans("", "", string.punctuation))

    return text.split()


def make_graph(words):
    g = Graph()

    previous = None

    for word in words:
        word_vertex = g.get_vertex(word)

        if previous:
            previous.increment_edge(word_vertex)

        previous = word_vertex

    g.generate_probability_mappings()

    return g


def compose(g, words, length=100):
    composition = []
    word = g.get_vertex(random.choice(words))

    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition


def main(artist):
    words = []
    for song_file in os.listdir(f"songs/{artist}"):  # here we get the words of each song of the artist
        if song_file == '.DS_Store': # there was some issue with this song file where it could not be read properly?
            continue
        song_words = get_words_from_text(f"songs/{artist}/{song_file}")
        words.extend(song_words)

    g = make_graph(words)
    composition = compose(g, words, 100)

    return " ".join(composition)


if __name__ == "__main__":
    print(main("taylor_swift"))
