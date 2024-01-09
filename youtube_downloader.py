import sys
import requests
from pytube import YouTube
file_path_read = "list_url.txt"
folder='D:\learn prog\pytube downloader\keimii_live'


def progress_function(chunk, file_handle, bytes_remaining):
    global filesize
    filesize=chunk.filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()
    
i=0
with open(file_path_read, "r") as file:
    for line in file:
        # link="https://www.youtube.com/watch?v=M7YTcbOzj2M"
        link = line.strip() 
        yt =YouTube(link, on_progress_callback = progress_function)
        # yt_HD=yt.streams.filter(file_extension='mp4')
        
        i+=1
        print("bot1 ->",i,". ",yt.title," start download",link)
        try:
            
            yt_HD=yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            yt_HD.download(output_path=folder,filename=yt.title+'.mp4')
            print("bot1 ->",i,". ",yt.title," succeed ",link)
        except:
            print("bot1 ->",i,". ",yt.title,"fail",link)
        # yt_HD.download()
        
        # print("downloaded ",link)
print("youtube downloader1 finish") 




