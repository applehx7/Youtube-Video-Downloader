from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter.filedialog import askdirectory
from tkinter import ttk
from pytube import *
import tkinter.messagebox as msg


root = Tk()


root.geometry("700x500")
root.resizable(False,False)
img = Image.open('venv/img/Root_bg.jpg')
root_bg_img = ImageTk.PhotoImage(img)
my_label = Label(root, image=root_bg_img)
my_label.place(x=0, y=0, relwidth=1, relheight=1)
root.title("InFinitY St0N3 6 >.<")
icon = PhotoImage(file="venv/img/icon.png")
root.iconphoto(False, icon)

status_bar = StringVar()
status_bar.set("STATUS : READY!")

status_label = Label(textvariable=status_bar, bg="grey", font="HACK 10 bold italic")
status_label.pack(side=BOTTOM, fill=X)

def call_download():
    download()


def set_path():
    
    file_path = askdirectory()

    path.set(file_path)





link = StringVar()

link_input = Entry(textvariable=link,fg="#999999", bg="#000000",font="lucida 12", relief=GROOVE,width=45).pack(side=TOP,anchor="e", pady=(197,0), padx=(0,40))



path = StringVar()
path.set(os.getcwd())
path_entry = Entry(textvariable=path,width=30,fg="#999999", bg="#000000",font="lucida 12", relief=GROOVE,).pack(anchor="w",pady=(53,0),padx=(260,0))



Button(text="BROWSE!",relief=SUNKEN, bg="#3d3633",font="lucida 10 bold",fg="#666261",command=set_path).pack(side=TOP, anchor="e", padx=(0,30))




quality = ["Low Quality", "High Quality", "Audio Only"]

combo = ttk.Combobox(root, values=quality, state="readonly", font="lucida 11 italic")
combo.current(0)
combo.pack(side=RIGHT,padx=(0,50),pady=(0,95))


def download():
    global url
    url = link.get()
    status_bar.set("STATUS: Checking URL...\t PLEASE WAIT")
    status_label.update()

    folder = path.get()


    try:
        to_do = combo.get()
        url = link.get()

        if to_do == "Low Quality":
            status_bar.set("STATUS: Downloading Video...\t PLEASE WAIT")
            status_label.update()
            down = YouTube(url).streams.get_lowest_resolution()
            down.download(folder)



        if to_do == "High Quality":
            status_bar.set("STATUS: Downloading Video...\t PLEASE WAIT")
            status_label.update()
            down = YouTube(url).streams.get_highest_resolution()
            down.download(folder)

        if to_do == "Audio Only":
            status_bar.set("STATUS: Downloading Video...\t PLEASE WAIT")
            status_label.update()
            down = YouTube(url).streams.get_audio_only()
            down.download(folder)

        status_bar.set("STATUS : READY!")


    except Exception as th3erroR:
            msg.showerror("ERROR!",f"Error >> {th3erroR}")




iii = Image.open("venv/img/down.png")
but_img = ImageTk.PhotoImage(iii)
a_but = Button(root, text="DOWNLOAD!",relief=GROOVE,font="mono 12 bold italic", bg="#3b3a39",fg="#c9960a", command=call_download)
a_but.pack(side=LEFT,pady=(0,50),padx=(80,0))
a_but.config(highlightbackground="black")



root.mainloop()
