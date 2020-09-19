from pytube import *
from tkinter import *
from tkinter.filedialog import *
import tkinter
from PIL import Image, ImageTk
from tkinter.messagebox import *
from threading import *

file_size = 0
font = ('verdana', 20)

def completeDownload(stream, file_path):
    showinfo("Message", "File has been downloaded...")
    downloadBtn['text'] = "Start Download"
    downloadBtn['state'] = "active"
    urlField.delete(0, END)

def progressDownload(stream, chunk, bytes_remaining):
    percent = (100 * ((file_size - bytes_remaining) / file_size))
    downloadBtn['text'] = "{:00.0f}% downloaded ".format(percent)


def startDownload(url):
    global file_size
    path_to_save = askdirectory()
    if path_to_save is None:
        return

    try:
        ob = YouTube(url)
        stream = ob.streams.first()

        ob.register_on_complete_callback(completeDownload)
        ob.register_on_progress_callback(progressDownload)

        file_size = stream.filesize
        stream.download(output_path=path_to_save)

    except Exception as e:
        print(e)

def btnClicked():
    try:
        downloadBtn['text'] = "Download in Progress..."
        downloadBtn['state'] = 'disabled'
        url = urlField.get()
        if url == '':
            return
        thread = Thread(target=startDownload, args=(url,))
        thread.start()

    except Exception as e:
        print(e)

main = Tk()

# Setting title of window
main.title("YouTube Downloader")

# Setting Icon
img = tkinter.PhotoImage(file='Icon.gif')
main.tk.call('wm', 'iconphoto', main._w, img)

# Heading icon
img = ImageTk.PhotoImage(Image.open('Icon.png').resize((100, 100)))
headingIcon=Label(main, image=img)
headingIcon.image = img
headingIcon.pack(side=TOP, pady = 25)

# URL TextField
urlField = Entry(main, font=("verdana", 18), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10)

# Download button
downloadBtn = Button(main, text = "Start Downloading", font = ("verdana", 18), relief = 'ridge', command = btnClicked)
downloadBtn.pack(side=TOP, pady = 10)

# Setting the length and width of window
main.geometry("500x600")
main.mainloop()