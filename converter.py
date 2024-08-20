# Evan Yeomans 
# Youtube video converter

import yt_dlp as youtube_dl

# downloads yt_url to the same directory from which the script runs
def download_audio(yt_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'D:/Video/downs/%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])

# def main():
#     yt_url = input("Enter the youtube url: ")
#     download_audio(yt_url)

# main()