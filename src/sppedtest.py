from cgi import test
import tkinter as tk
from tkinter import Label, font
from speedtest import Speedtest


def updatetext(event=None):

    uploadvar.set("Working..")
    downloadvar.set("Working..")
    upload_label.update()
    download_label.update()
    speedtester = Speedtest()
    upload = speedtester.upload()
    download = speedtester.download()
    upload_speed = round(download / (10**6), 2)
    download_speed = round(upload / (10**6), 2)
    uploadvar.set(f"Upload Speed - {str(upload_speed)} Mbps")
    downloadvar.set(f"Download Speed - {str(download_speed)} Mbps")
    upload_label.update()
    download_label.update()


root = tk.Tk()
root.title("Speed Test")
root.geometry("500x588")

testBtn = tk.Button(root, text="GO!", font=(
    "Comic Sans Ms", 14, font.BOLD), command=updatetext)

testBtn.place(x=500/2-15, y=588/2-15)

uploadvar = tk.StringVar()
upload_label = Label(textvariable=uploadvar, font=("Verdana", 18))

downloadvar = tk.StringVar()
download_label = Label(textvariable=downloadvar, font=("Verdana", 18))

# packing the labels

download_label.pack(side="top")
upload_label.pack(side="top")


root.mainloop()
