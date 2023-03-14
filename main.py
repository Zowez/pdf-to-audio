import pyttsx3
import PyPDF2
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


filepath = ""

def open_file():
    global filepath
    filepath = filedialog.askopenfilename(filetypes=(("pdf files","*.pdf"),("all files","*.*")),title="Chose PDF")
    return filepath


def convert(filepath):
    if filepath == "":
        messagebox.showwarning(title="Choso a file!",message="You dont chose any file!")
    else:
        file = open(f"{filepath}", "rb")
        pdf = PyPDF2.PdfReader(file)
        speaker = pyttsx3.init()
        text = ""
        for num in range(len(pdf.pages)):
            page = pdf.pages[num]
            text += page.extract_text()

        speaker.save_to_file(f"{text}","test.mp3")
        speaker.runAndWait()

window = Tk()
window.config(padx=30,pady=30 )

title = Label(text="PDF to MP3")
title.pack()
open_file_button = Button(text="Chose PDF", command=open_file)
open_file_button.pack()


convert_button = Button(text="Convert", command=lambda: convert(filepath=filepath))
convert_button.pack()


window.mainloop()
