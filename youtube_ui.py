import tkinter as tk 
import tkinter.scrolledtext as st 
from tkinter import filedialog
import youtube_downloader as yd

root = tk.Tk() 
root.title("ScrolledText Widget")

# Title Label 
tk.Label(root,text = "Youtube Downlaoder",  
            font = ("Times New Roman", 12),  
            background = 'green',  
            foreground = "white").grid(column = 0,row = 0) 

#playlist get link
entry1 = tk.Entry(root) 
entry1.grid()


#text_area
text_area = st.ScrolledText(root, 
                            width = 50,  
                            height = 8,  
                            font = ("Times New Roman",12)
                            ).grid(column = 0, pady = 10, padx = 10)


def get_mp3():
    playlist = entry1.get()
    print(playlist)
    folder_path = filedialog.askdirectory()
    print(folder_path)
    yd.get_youtube_mp3(playlist, folder_path)
button3 = tk.Button(root, text=" MP3 downloader ", command=get_mp3)
button3.grid( sticky="nsew")


def get_mp4():
    playlist = entry1.get()
    print(playlist)
    folder_path = filedialog.askdirectory()
    print(folder_path)
    yd.get_youtube_mp4(playlist, folder_path)
button2 = tk.Button(root, text=" M4 downlaoder", command =get_mp4)
button2.grid(  sticky="nsew")



root.mainloop()
