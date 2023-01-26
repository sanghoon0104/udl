import moviepy.editor as meditor
from moviepy.video.io.VideoFileClip import VideoFileClip
import os, glob

fpath = os.getcwd()
files = glob.glob(fpath + '/*.mp4')  # .mp4 파일만 대상
print(files)
# ['./python_pytube/youtube\\[케스코뉴스] 휴그린 리모델링 최초 자동환기창 시공 기업.mp4']

for file in files:
    mfile = meditor.VideoFileClip(file)
    print(mfile)
    # <moviepy.video.io.VideoFileClip.VideoFileClip object at>
    filename = os.path.splitext(file)
    mfile.audio.write_audiofile(filename[0] + '.mp3')