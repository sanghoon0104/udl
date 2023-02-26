import urllib.request
import time
from pytube import YouTube
# 다운받을 이미지 url
url = "https://www.youtube.com/watch?v=drYAEQt8HE0"

yt = YouTube(url)
stream = yt.streams.get_highest_resolution().download()
# time check
start = time.time()

# 이미지 요청 및 다운로드
urllib.request.urlretrieve( yt.thumbnail_url, yt.title )

# 이미지 다운로드 시간 체크
print(time.time() - start)