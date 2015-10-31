__author__ = 'William'

import random
import os
from glob import glob


def _filter_mp3_files(directory_root):
    return [y for x in os.walk(directory_root) for y in glob(os.path.join(x[0], "*.mp3"))]


def _generate_random_list(song_list, number_of_songs):
    random_list = []

    for count in range(0, len(song_list)):
        list_length = len(song_list)
        random_number = random.randrange(0, list_length)
        song = song_list[random_number]
        random_list.append(song)
        song_list.remove(song)
        if count == (number_of_songs - 1):
            break
    return random_list


def _print_list(list_to_print):
    for song in list_to_print:
        print(song)


def _write_list_to_file(song_list):
    playlist_file_path = r"C:\Users\William\Music\Playlists\PlaylistGen.m3u", "wt"

    with open(playlist_file_path) as playlist_file:
        for song in song_list:
            playlist_file.write("{0}\n".format(song))


def main():
    try:
        number_of_songs = int(input("Enter number of songs: "))
    except ValueError:
        print("Not a number!")
        main()

    print("Generating playlist...")
    directory_root = r"D:\Music"
    song_list = _filter_mp3_files(directory_root)
    random_list = _generate_random_list(song_list, number_of_songs)
    _print_list(random_list)
    _write_list_to_file(random_list)
    input("\nDone! Press Return to exit: ")

main()
