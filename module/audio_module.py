from pytube import Playlist  , YouTube
import glob , os
import os.path
from moviepy.video.io.VideoFileClip import VideoFileClip
import moviepy.editor as meditor
import eyed3
import urllib.request

def playlistdownload() :
    p = Playlist(input("재생목록에 있는 영상중 아무 영상의 url을 입력하세요: "))
    for video in p.videos:
        video.streams.get_highest_resolution().download()
        print(video.title)
        print(video.thumbnail_url)
        #converting mp4 to mp3 and adding album art
        fpath = os.getcwd()
        files = glob.glob(fpath + '/*.mp4')  # .mp4 files only
        print(files)
        for file in files:
            mfile = meditor.VideoFileClip(file)
            filename = os.path.splitext(file)
            mfile.audio.write_audiofile(filename[0] + '.mp3')
            mfile.close()
            [os.remove(f) for f in glob.glob('*.mp4')]
            #Adding album art cover
            new_file = file.replace('.mp4', '.mp3')
            audiofile = eyed3.load(new_file)
            response = urllib.request.urlopen(video.thumbnail_url)
            imagedata = response.read()
            audiofile.tag.images.set(3, imagedata, "image/jpeg", u"cover")
            audiofile.tag.save()
            print("success")


def videodown() :
    par = list(input("다운로드 할 유튜브 url 입력(띄어쓰기로 다중 다운로드 가능): ").split())
    for i in par :
        yt = YouTube(i)
        yt.streams.get_highest_resolution().download()
        print(yt.title)
        print(yt.thumbnail_url)
        fpath = os.getcwd()
        files = glob.glob(fpath + '/*.mp4')  # .mp4 files only
        print(files)
        for file in files:
            mfile = meditor.VideoFileClip(file)
            filename = os.path.splitext(file)
            mpg = mfile.audio.write_audiofile(filename[0] + '.mp3')
            mfile.close()
            [os.remove(f) for f in glob.glob('*.mp4')]
            #Adding album art cover
            new_file = file.replace('.mp4', '.mp3')
            audiofile = eyed3.load(new_file)
            response = urllib.request.urlopen(yt.thumbnail_url)
            imagedata = response.read()
            audiofile.tag.images.set(3, imagedata, "image/jpeg", u"cover")
            audiofile.tag.save()
            print('success')

a = int(input('재생목록 다운로드 1번 아니면 2번: '))
if a == 1 :
    playlistdownload()
else:
    videodown()