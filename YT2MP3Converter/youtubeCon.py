from __future__ import unicode_literals
import youtube_dl
import sys
import os
from mutagen.id3 import ID3, APIC
from mutagen.easyid3 import EasyID3

#downloadMP3 will download the file, convert to MP3, then return the filename.
def downloadMP3(URL):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(URL)
        filename = ydl.prepare_filename(info)
        return filename[:-4] + "mp3"

def editMetaData(filename, imageSRC, title, artist, album):
    audio = ID3(filename)
    with open(imageSRC, 'rb') as albumart:
        audio['APIC'] = APIC(
                        encoding=3,
                        mime='image/jpeg',
                        type=3, desc=u'Cover',
                        data=albumart.read()
                        )
    audio.save()

    metatag = EasyID3(filename)
    metatag['title'] = title
    metatag['artist'] = artist
    metatag['album'] = album
    metatag.save()

'''
convert is the entire routine:
    -> Download the Youtube and convert to an MP3
    -> Take the MP3 and add the proper metadata
        -Title
        -Artist
        -Album
        -Album Art
    -> Move the file to iTunes
'''
def convert(song):
    songInfo = song.split(", ")

    if len(songInfo) != 5:
        print("USAGE ERROR: [youtubeURL] [albumArt] [title] [artist] [album]")
        return

    URL = songInfo[0]
    albumArt = songInfo[1]
    title = songInfo[2]
    artist = songInfo[3]
    album = songInfo[4]

    try:
        #convert YT to MP3
        filename = downloadMP3(URL)
        os.rename(filename, title + ".mp3")
        filename = title + ".mp3"

        #edit meta data
        editMetaData(filename, albumArt, title, artist, album)

        #move the file to the iTunes folder
        os.rename(filename, "C:/Users/lildu/Music/iTunes/iTunes Media/Automatically Add to iTunes/{}".format(filename))

        print("{} by {}, is now added to iTunes".format(title, artist))
        emptyString = ""
        return emptyString
    
    except:
        print("{} by {} failed to be added, check the album art lol")
        return title

#this should open a text file and convert every single line
def parseTextFile(file):
    f = open(file, "r")
    failList = []
    for song in f:
        value = convert(song)
        if value != "":
            failList.append(value)
    f.close()
    print("The following failed, consider checking them:")
    print(failList)

if __name__ == "__main__":
    parseTextFile(sys.argv[1])