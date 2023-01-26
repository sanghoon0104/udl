from pytube import *

# DOWNLOAD_FOLDER = "C:\\Users\\sanghoon\\Desktop"
url = "https://www.youtube.com/watch?v=X8jjlicVUyY"
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download()


