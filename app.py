from tkinter import *
from tkinter import filedialog
from pytube import Playlist
from pytube import YouTube
from tqdm import tqdm

root = Tk()
root.title("YouTube Downloader")
# root.iconbitmap("E:/FCAI/Level_2/Term_2/DataBase/Project/database.ico")
root.geometry("800x400")


def main():

    def clear():
        # Clear entries
        htype.delete(0, END)
        # size.delete(0, END)

    file_path = None
    def select_path():
        file_path = filedialog.askdirectory()
        Label(root, text=f'Path: {file_path}').grid(row=3, column=1, columnspan=2)

    def download_video():
        

    # Title
    title_lable = Label(root, text="Playlist Downloader")
    title_lable.grid(row=0, column=1, columnspan=2)

    # Lable & Entry
    house_type = Label(root, text="Playlist URL:")
    house_type.grid(row=2, column=1)
    htype = Entry(root, width=70)
    htype.grid(row=2, column=2)

    download_path = Button(root, text="Select download folder", command=select_path)
    download_path.grid(row=3, column=0, columnspan=2, padx=10, pady=10, ipadx=0)

    # Submit button
    # clear_data = Button(root, text="Clear Input", command=clear)
    # clear_data.grid(row=5, column=3, columnspan=1, padx=5, pady=10, ipadx=70)
    data_submit = Button(root, text="Download")
    data_submit.grid(row=5, column=3, columnspan=1, padx=5, pady=10, ipadx=70)


main()
root.mainloop()
