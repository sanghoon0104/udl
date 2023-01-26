from pytube import Playlist
import glob
import os.path



def playlistdownload() :
    p = Playlist(input("재생목록에 있는 영상중 아무 영상의 url을 입력하세요: "))
    for video in p.videos:
        video.streams.filter(only_audio=True).first().download()

playlistdownload()        


# def playlistdownload() :
#     p = Playlist(input("재생목록에 있는 영상중 아무 영상의 url을 입력하세요: "))
#     for video in p.videos:
#         video.streams.filter(only_audio=True).first().download()

# files = glob.glob("*.mp4")
# for x in files:
# 	if not os.path.isdir(x):
# 		filename = os.path.splitext(x)
# 		try:
# 			os.rename(x,filename[0] + '.mp3')
# 		except:
# 			pass