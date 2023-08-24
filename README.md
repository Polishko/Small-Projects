# Small-Projects
This repository contains small beginner level Python projects from the Internet where I try to apply learning into practice.

# binary_search (free_code_camp, kyling18)
This small project is a sligthly adapted version from that provided by @free_code_camp. The purpose is to compare searching linearly vs. in a binary manner in Python and show that binary search is faster than linear search. Two separate functions are provided for the purpose of searching linearly and with binary search, respectively. Then, using the random library in Python, a sorted list containing randomly generated integers in a given range and of length 10000 is created. The time library is used to calculate the different amount of time it takes for the two functions to find a given target number in the list.

# graph_composer (free_code_camp, kyling18)
Another small project from @free_code_camp created by @kyling18. It aims to generate new text using an existing text based on the weight of words in the text and using Markov Chain relationship for the purpose. The weight is indirectly determined by the count of the words in the text. Here I try to practice using classes and I also learn a little about new concepts such as vertices, nodes, edges and graph construction.

- The initial version is the basic code, where the random library is used to select words based on their weights, but there's still little meaning in the final text.
- The second version mainly targets song text, introduces a more sofisticated way of taking text files from directories without hard-coding the file name. The songs in the song list are those selected by the author and I will introduce new ones in another version.
- The third version will contain further modifications of my own. For now I added a code that could be used to get song lyrics with the lyricsgenius library from Genius.com. I wrote my own version for this file using some tips from https://melaniewalsh.github.io/Intro-Cultural-Analytics/04-Data-Collection/07-Genius-API.html
The code creates folders with the names of the artists from a user defined list, adds them to a user defined directory, then searches for defined maximum number of songs using the lyricsgenius library and adds their lyrics into txt files under the artist folder.
