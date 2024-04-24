import re
import tkinter as tk
from pytube import YouTube
import customtkinter
from pytube import Playlist

def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)} %")

class GUI:
    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.app = customtkinter.CTk()
        self.app.geometry("720x480")
        self.app.title("YouTube Downloader")

        self.title = customtkinter.CTkLabel(self.app, text="Enter a YouTube link", width=200, height=30, font=("cursive", 28))
        
        # # this as a url placeholder
        # self.url_placeholder = customtkinter.CTkLabel(self.app, text="")
        # self.url_placeholder.configure(text="Enter you url", text_color="white")
        # self.url_placeholder.pack()
        self.url_input = tk.StringVar()
        self.url = customtkinter.CTkEntry(self.app, width=500, height=30, textvariable=self.url_input, placeholder_text="Enter a YouTube link")
    
        self.path_button = customtkinter.CTkButton(self.app, text="Choose Download Directory", command=lambda: self.select_path())
            
        self.finish_label = customtkinter.CTkLabel(self.app, text="")
        self.display_path_label = customtkinter.CTkLabel(self.app, text="")

        self.progress_bar = customtkinter.CTkProgressBar(self.app, width=400)
        self.progress_pct = customtkinter.CTkLabel(self.app, text="")
        self.progress_bar.set(0)
        
        self.download_hq = customtkinter.CTkButton(self.app, text="Download High Quality (.mp4)", command=lambda: self.download_video("HighQuality"))
        self.download_lq = customtkinter.CTkButton(self.app, text="Download Low Quality (.mp4)", command=lambda: self.download_video("LowQuality"))
        self.download_audio = customtkinter.CTkButton(self.app, text="Download Audio Only (.mp3)", command=lambda: self.download_video("Audio"))
        self.download_plist_audio = customtkinter.CTkButton(self.app, text="Download Playlist Audio Only (.mp3)", command=lambda: self.download_playlist(self.url))
        

    def select_path(self):
        self.download_path = customtkinter.filedialog.askdirectory()
        self.display_path_label.configure(text=f"{self.download_path}", text_color="white")

    def download_video(self, option):
        video_url = self.url.get()
        yt = YouTube(video_url, on_complete_callback=on_progress)
        if option == "HighQuality":
            video = yt.streams.get_highest_resolution()
        
        elif option == "LowQuality":
            video = yt.streams.get_lowest_resolution()
        
        elif option == "Audio":
            video = yt.streams.get_audio_only()
        else:
            return
        
        self.title.configure(text=yt.title, text_color="white")
        self.finish_label.configure(text="")
        video.download(self.download_path) # todo: if path no entered
        self.finish_label.configure(text="Video Downloaded", text_color="green")

    def download_playlist(self, url):
        '''
        Download the audio track only for the playlist 
        '''
        playlist_url = url.get()
        playlist = Playlist(playlist_url)

        # this fixes the empty playlist.videos list
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

        for video in playlist.videos:
            audioStream = video.streams.get_audio_only()
            audioStream.download(self.download_path)
        
        self.finish_label.configure(text="Video Downloaded", text_color="green")
    
    def on_progress(self, stream, bytes_remaining):
        total_size = stream.filesize
        print(type(total_size), type(bytes_remaining))
        bytes_downloaded = total_size - int(float(bytes_remaining))
        completion_pct =bytes_downloaded / total_size * 100
        pct_string = str(completion_pct(int(completion_pct)))
        self.progress_prt.configure(text=pct_string + "%")
        self.progress_pct.update()
        self.progress_bar.set(float(completion_pct) / 100)

    def display(self,):
        self.title.pack(padx=10, pady=10)
        self.url.pack()
        self.finish_label.pack()
        self.path_button.pack(padx=10, pady=0, ipadx=200)
        self.display_path_label.pack()
        self.download_hq.pack(padx=10, pady=10)
        self.download_lq.pack(padx=10, pady=10)
        self.download_audio.pack(padx=10, pady=10)
        self.download_plist_audio.pack(padx=10, pady=10)
        self.progress_bar.pack(pady=10, after=self.url)
        self.progress_pct.pack(after=self.progress_bar)
        self.app.mainloop()


gui = GUI()
gui.display()