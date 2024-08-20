# GUI for Youtube-mp3 converter

from time import sleep
import customtkinter
import yt_dlp as youtube_dl
from converter import download_audio

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x400")

def downloader(url):
    # Fetch video information
    with youtube_dl.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', 'Unknown Title')

    # Display the video title and download status
    new_text = customtkinter.CTkTextbox(master=frame, width=400, height=50)
    new_text.insert("1.0", f"Downloaded '{video_title}'")
    new_text.pack(pady=12, padx=10)
       

    # Call the download_audio function with the URL
    download_audio(url)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=40, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Convert Youtube video to mp3")
label.pack(pady=12, padx = 10)

entry = customtkinter.CTkEntry(master=frame, placeholder_text="Enter the youtube url")
entry.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Download", command=lambda: downloader(entry.get()))
button.pack(pady=12, padx=10)

root.mainloop()