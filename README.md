# YouTube-to-MP3-Converter
This is a python script to help me streamline my youtube to mp3 converting, so that I can make playlists for the road.

#Requirements:
    -Python 2.7
    -Libraries: (Use "python pip install")
        -youtube.dl (https://pypi.org/project/youtube_dl/)
        -mutagen (https://mutagen.readthedocs.io/en/latest/index.html)

#How to use it:

Git clone the repository.

Create a text file (i.e. SongList.txt) that has lines organized like this (make sure to deliniate with commas):
[youtubeURL],[albumArt],[title],[artist],[album]

youtubeURL: the URL in which you want the song downloaded as
albumArt: the location of the album art, if you place it into the pictures folder, "./pictures/nameOfPicture.jpg"
title: title of song
artist: artist of song
album: ablbum of song

on line 83 of youtubeCon.py: os.rename(filename, "D:/iTunes/Automatically Add to iTunes/{}".format(filename)), you want to change "D:/iTunes/Automatically Add to iTunes/{}" to the directory of your Automatically Add to iTunes folder. Don't forget to save!

Then after that, you can go ahead and run the script with the text file.

youtubeCon.py SongList.txt

It should go through each line and then achieve what you want.