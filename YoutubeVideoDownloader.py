from tkinter import *
from tkinter import ttk
from pytube import YouTube
from tkinter import filedialog

root = Tk()
root.geometry("750x600")
root.title("YouTube Video Downloader")
root.columnconfigure(0, weight=1)

folderName = ""


# Functions

# for choosing file location

def Location():
    global folderName
    folderName = filedialog.askdirectory()
    if len(folderName) > 1:
        locationError.config(text="Your file will be saved in " + folderName, fg='green')
    else:
        locationError.config(text="Invalid Location, Please choose a valid path.")


# Download Video

def Download():
    global stream
    choice = qualityCombobox.get()
    url = linkentry.get()

    if len(url) > 1:
        linkError.config(text="Downloading...", fg="green")
        yt = YouTube(url)

        if choice == Choices[0]:
            stream = yt.streams.filter(progressive=TRUE).first()
        elif choice == Choices[1]:
            stream = yt.streams.filter(progressive=TRUE, file_extension='mp4', res='360p').last()
        #elif choice == Choices[2]:
           # stream = yt.streams.filter(progressive=TRUE, file_extension='mp4', res='144p').last
        elif choice == Choices[2]:
            stream = yt.streams.filter(only_audio=TRUE).first()
        else:
            linkError.config(text="Paste link again", fg='red')
    # Download
    statusVar.set("Downloading your video...")
    sbar.update()
    stream.download(folderName)
    linkError.config(text="Download Completed", fg='green')
    statusVar.set("Download completed...")
    sbar.update()


# frames

frame0 = Frame(root, bg='white', relief=RIDGE, borderwidth=8)
frame0.pack(side=TOP, fill=X, padx=1, pady=10)
frame1 = Frame(root, bg='white', relief=FLAT, borderwidth=4)
frame1.pack(side=TOP, fill=X, padx=1)
frame2 = Frame(root, bg='white', relief=FLAT, borderwidth=4)
frame2.pack(side=TOP, fill=X, padx=1)

# Priject Title Label

title = Label(frame0, text="YouTube Video Downloader", bg="red", fg='white', height=2, font="Times 36 bold",
              relief=FLAT)
title.pack(fill=X)

# Label for linkInput

link = Label(frame1, text="Enter the URL of Video below ", bg="white", fg='black', font="Times 20 bold", relief=RAISED)
link.pack(fill=X, anchor=N, side=TOP, pady=2)

# Entryfield for Link

linkvar = StringVar()
linkvar = ""
linkentry = Entry(frame1, textvariable=linkvar, font="Times 20 italic", width=40, relief=FLAT, bg="light grey")
linkentry.pack(side=TOP, padx=10, pady=15)

# Error msg in case of invalid Link

linkError = Label(frame1, text="The link you entered is Invalid", fg='white', bg='white')
linkError.pack(side=TOP)

# Location for saving the file

saveLocation = Label(frame1, text="Choose the location where you want to save your file"
                                  " ", bg="white", fg='black', font="Times 14 ", relief=RIDGE)
saveLocation.pack(fill=X, side=LEFT, pady=2, padx=60, ipadx=30)

# Button for Path

butPath = Button(frame1, text="Choose Path", bg='red', fg='white', relief=RIDGE, command=Location)
butPath.pack(side=LEFT, pady=2, ipadx=10)

# Error msg in case of invalid path

locationError = Label(frame2, text="The path you entered is Invalid", fg='WHITE', bg='white')
locationError.pack(side=TOP)

# Video Quality Label

linkError = Label(frame2, text="Select Quality", fg='black', bg='white', font="Times 26 bold ", relief=SUNKEN)
linkError.pack(side=TOP, pady=25, fill=X)

# Choices
Choices = ['720p', '360p', 'Audio file']
qualityCombobox = ttk.Combobox(frame2, value=Choices, width=25, font="fost 12 italic")
qualityCombobox.pack(side=TOP)

# Download Button

DwnldButton = Button(frame2, text="Download", bg='red', fg='white', relief=RIDGE, width=14, font="Times 26 bold italic",
                     command=Download)
DwnldButton.pack(side=TOP, pady=20, ipadx=10)

#Status bar
statusVar = StringVar()
statusVar.set("")

sbar = Label(frame2, textvariable=statusVar, relief=RIDGE,anchor = W)
sbar.pack(fill = X, side = BOTTOM)

root.mainloop()
