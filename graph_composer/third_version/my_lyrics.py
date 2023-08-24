# get an api_key from https://genius.com/api-clients and save it securely in a file

import api_key # the file that contains your api key
import lyricsgenius
import os

client_access_token = api_key.my_client_access_token

artists = ["Diana Ross", "Stevie Wonder", "Tom Browne", "Genesis"]  # add your own list of artists
parent_dir = "some_dir_path" # the main directory that will contain artist name folders with their song files
genius = lyricsgenius.Genius(client_access_token)


def add_lyrics(artists_list, max_song_count):  # Write lyrics of given count of songs by each artist in the list
    # create directory for each artist
    for name in artists_list:
        directory = name
        path = os.path.join(parent_dir, directory)

        try:
            os.mkdir(path)
        except OSError:
            continue
            
    # add songs for each artist
    for name in artists_list:
        path = f"{parent_dir}/{name}"
        try:
            songs = (genius.search_artist(name, max_songs=max_song_count, sort="popularity")).songs

            for song in songs:
                file_name = song.title
                with open(os.path.join(path, f"{file_name}.txt"), "w") as f:
                    lyrics = song.lyrics
                    f.write(lyrics)
        except: # in case of encountering some error while getting the songs
            pass


add_lyrics(artists, 4)
