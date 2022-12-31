from pytube import YouTube
import glob
import os.path
par = list(input("다운로드 할 유튜브 url 입력 : ").split())
 

for i in par :
    yt = YouTube(i)
    yt.streams.filter(only_audio=True).all()

    yt.streams.filter(only_audio=True).first().download()
    print('success')

    files = glob.glob("*.mp4")
    for x in files:
        if not os.path.isdir(x):
            filename = os.path.splitext(x)
            try:
                os.rename(x,filename[0] + '.mp3')
            except:
                pass
    