from pytube import Playlist, YouTube
from moviepy.editor import *

fpath = "C:\\Users\\sanghoon\\Desktop"
url = "https://www.youtube.com/watch?v=X8jjlicVUyY"
audiofile = "C:\\Users\\sanghoon\\udl\\audio"
videofile = "C:\\Users\\sanghoon\\udl\\video"
def ydown():
    yt = YouTube(url)

    vpath = (
        yt.streams.filter(adaptive=True, file_extension="mp4", only_video=True)
        .order_by("resolution")
        .desc()
        .first()
        .download(videofile)
    )

    apath = (
        yt.streams.filter(adaptive=True, file_extension="mp4", only_audio=True)
        .order_by("abr")
        .desc()
        .first()
        .download(audiofile)
    )

    v = VideoFileClip(vpath)
    a = AudioFileClip(apath)

    v.audio = a
    v.write_videofile(("new.mp4"))


def playlistdown(url):
    pl = Playlist(url)

    for v in pl.video_urls:
        try:
            ydown(v)
        except:
            continue

ydown()