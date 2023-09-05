import tkinter
import customtkinter
from pytube import YouTube
import threading

resList = ["360p","720p"]
formatList = ["mp4","mp3"]

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_by_resolution(resolution=resSec.get())
        title.configure(text=ytObject.title, text_color="black")
        video.download()
        finishLabel.configure(text="Download Completed", text_color="black")
    except:
        finishLabel.configure(text="Download Error", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    POCompletetion = bytes_downloaded / total_size * 100
    per = str(int(POCompletetion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    # Update progress bar
    progressBar.set(float(POCompletetion) / 100)
    app.update()
    

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a Youtube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40,textvariable=url_var)
link.pack()

# Resolution Selector
resSec = customtkinter.CTkComboBox(app, values=resList)
resSec.set("Select Resolution")
resSec.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

#Progress Bar
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Run app
app.mainloop()