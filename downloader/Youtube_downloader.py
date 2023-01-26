from pytube import Playlist
from pytube import YouTube
from pytube.cli import on_progress
import glob
import os.path
yes = "Y"
no = "n"

def convertQM():
    answer = str(input("mp3파일로 변환? (Y/n) : " ))
    if answer == yes :
        answer2 = str(input("ffmpeg가 설치된 환경인가요?(Y/n/모름):"))
        if answer2 == yes:
            import moviepy.editor as meditor
            from moviepy.video.io.VideoFileClip import VideoFileClip
            fpath = os.getcwd()
            files = glob.glob(fpath + '/*.mp4')
            print(files)
            for file in files:
                mfile = meditor.VideoFileClip(file)
                print(mfile)
                filename = os.path.splitext(file)
                mfile.audio.write_audiofile(filename[0] + '.mp3')
        elif answer2 == no or answer2 == "모름" :
            files = glob.glob("*.mp4")
            for x in files:
                if not os.path.isdir(x):
                    filename = os.path.splitext(x)
                    try:
                        os.rename(x,filename[0] + '.mp3')
                    except:
                        pass
    else:
        print("mp3 변환 취소")

def downloadpl() :
    p = Playlist(input("재생목록에 있는 영상중 아무 영상의 url을 입력하세요: "))
    for video in p.videos:
        video.streams.get_highest_resolution().download()
        print("제목 : ", video.title)
        print("길이 : ", video.length)
        print("게시자 : ", video.author)
        print("게시날짜 : ", video.publish_date)
        print("조회수 : ", video.views)
        print("키워드 : ", video.keywords)
        print("설명 : ", video.description)
        print("썸네일 : ", video.thumbnail_url)
        print('success')
        
def downloadonly() :
    par = list(input("다운로드 할 유튜브 url 입력(띄어쓰기로 다중 다운로드 가능): ").split())
    for i in par :
        yt = YouTube(i)
        print("제목 : ", yt.title)
        print("길이 : ", yt.length)
        print("게시자 : ", yt.author)
        print("게시날짜 : ", yt.publish_date)
        print("조회수 : ", yt.views)
        print("키워드 : ", yt.keywords)
        print("설명 : ", yt.description)
        print("썸네일 : ", yt.thumbnail_url)
        print('success')
        yt.streams.get_highest_resolution().download()
        
def delete() :
    secanswer = int(input("mp4파일 삭제:ffmpeg설치 환경인 경우(1) 아니면 (2): "))
    if secanswer == 1 :
        [os.remove(f) for f in glob.glob('*.mp4')]
    elif secanswer == 2:
        print("success")



print("Please read 'README'")
firstanswer = int(input("영상 다운로드(1) 재생목록 다운로드(2) 영상다운로드 하지않음(3): "))
if firstanswer == 1 :
    downloadonly()
    convertQM()
    delete()
elif firstanswer == 2 :
    downloadpl()
    convertQM()
    delete()
elif firstanswer == 3 :
    convertQM()
    delete()
    









