
from pytube import Playlist  , YouTube
import glob , os
import os.path
from moviepy.video.io.VideoFileClip import VideoFileClip
import moviepy.editor as meditor
import eyed3
import urllib.request

def set_artist() :

        fpath = os.getcwd()
        files = glob.glob(fpath + '/*.mp3')  # .mp4 files only
        print(files)
        i = int(0)
        for file in files:
            #Adding album art cover
            new_file = file
            audiofile = eyed3.load(new_file)
            audiofile.tag.artist = u"SZA"
            audiofile.tag.save()
            print("success")
    #     self.title = title
    #     self.artist = artist
    #     self.album = album
    #     self.album_artist = album_artist
    #     self.track_num = track_num

#set_artist()

def albumdl() :
    p = Playlist(input("재생목록에 있는 영상중 아무 영상의 url을 입력하세요: "))
    artist = (str(input("가수 입력:")))
    album = (str(input("앨범 이름 입력: ")))
    i = 0
    for video in p.videos:
        video.streams.get_highest_resolution().download()
        print(video.title)
        print(video.thumbnail_url)
        #converting mp4 to mp3 and adding album art
        fpath = os.getcwd()
        files = glob.glob(fpath + '/*.mp4')  # .mp4 files only
        print(files)
        for file in files:
            i += 1
            mfile = meditor.VideoFileClip(file)
            filename = os.path.splitext(file)
            mfile.audio.write_audiofile(filename[0] + '.mp3')
            mfile.close()
            [os.remove(f) for f in glob.glob('*.mp4')]
            #Adding album art cover
            new_file = file.replace('.mp4', '.mp3')
            audiofile = eyed3.load(new_file)
            response = urllib.request.urlopen(video.thumbnail_url)
            print("download img")
            imagedata = response.read()
            audiofile.tag.images.set(3, imagedata, "image/jpeg", u"cover")
            audiofile.tag.artist = artist
            audiofile.tag.album = album
            audiofile.tag.album_artist = artist
            audiofile.tag.track_num = i
            audiofile.tag.save()
            print("success")

albumdl()