from pytube import YouTube
import moviepy.editor as meditor
from moviepy.video.io.VideoFileClip import VideoFileClip
import os, glob
import eyed3
import urllib.request

#downloading youtube video
url = "https://www.youtube.com/watch?v=X8jjlicVUyY"
yt = YouTube(url)
print(yt.title)
print(yt.thumbnail_url)
stream = yt.streams.get_highest_resolution()
stream.download()

def ConvertAndAdd():
    #converting mp4 to mp3 and adding album art
    fpath = os.getcwd()
    files = glob.glob(fpath + '/*.mp4')  # .mp4 files only
    print(files)
    for file in files:
        mfile = meditor.VideoFileClip(file)
        filename = os.path.splitext(file)
        mfile.audio.write_audiofile(filename[0] + '.mp3')
        #Adding album art cover        
        new_file = file.replace('.mp4', '.mp3')
        print(new_file)
        audiofile = eyed3.load(new_file)
        response = urllib.request.urlopen(yt.thumbnail_url)
        imagedata = response.read()
        audiofile.tag.images.set(3, imagedata, "image/jpeg", u"cover")
        audiofile.tag.save()
ConvertAndAdd()
#Read image from local file (for demonstration and future readers)
# with open('C:/Users/sanghoon/udl/save.jpg', "rb") as image_file:
#      imagedata = image_file.read()
# audiofile.tag.images.set(3, imagedata, "image/jpeg", u"cover")
# audiofile.tag.save()