# YouTube-to-MP3-Converter
This is a python script to help me streamline my youtube to mp3 converting, so that I can make playlists for the road.

## Requirements:
- Python 2.7
- Libraries: (Use "python pip install")
    - youtube.dl (https://pypi.org/project/youtube_dl/)
    - mutagen (https://mutagen.readthedocs.io/en/latest/index.html)

## How to use it:

1. Git clone the repository.

2. Create a text file (i.e. SongList.txt) that has lines organized like this (make sure to deliniate with commas):
[youtubeURL],[albumArt],[title],[artist],[album]

```
youtubeURL: the URL in which you want the song downloaded as
albumArt: the location of the album art, if you place it into the pictures folder, "./pictures/nameOfPicture.jpg"
title: title of song
artist: artist of song
album: ablbum of song
```

here's an example:
https://youtu.be/Lur-rvf6A1c,./pictures/380.png,Clarity,Zedd,Clarity

3. On line 94 of youtubeCon.py:

    ```os.rename(filename, "C:/Users/theal/Music/iTunes/iTunes Media/Automatically Add to iTunes/{}")```

    you want to change

    ```"D:/iTunes/Automatically Add to iTunes/{}"```

to the directory of your Automatically Add to iTunes folder and don't forget to save!

4. Then after that, you can go ahead and run the script with the text file.

    ```youtubeCon.py SongList.txt```

    It should go through each line and then achieve what you want. If there are usage error's it will skip to the next song to download and will let you know what song is incorrectly formatted. 

## Disclaimer
1. Sometimes youtube links can be finicky so be aware of that. 
2. Lastly the songs name, artist name, and albums cannot have special characters (such as \/?<>) as windows is lowkey a POS. I also suck at programming so no commas are allowed, I am sure that if I spent a couple more minutes I can also figure out how to let them be in them, but alas I am lazy, so take it or leave it lol.