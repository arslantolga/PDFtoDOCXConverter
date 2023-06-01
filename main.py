from pdf2docx import Converter
import tkinter
from tkinter import filedialog

FONT = ('Helvetica', 12)

window = tkinter.Tk()
window.geometry("400x300")
window.title("PDF to DOCX Converter")
def choose():
    pdf_filename = filedialog.askopenfilenames()

    ana_dizin = pdf_filename[0]
    ayrilmis = ana_dizin.split("/")
    file_name = ayrilmis[-1]
    del ayrilmis[-1]
    birlesik = "/".join(ayrilmis)
    birlesik = birlesik + f"/{file_name}.docx"

    cv = Converter(pdf_filename[0])
    cv.convert(birlesik)
    cv.close()
    result_label.config(text="File Created", font=FONT, pady=30)
    result_label.pack()


label = tkinter.Label(text="Choose Your PDF File", font=FONT, pady=30)
label.pack()

button = tkinter.Button(text="Choose",command=choose)
button.pack()

result_label = tkinter.Label(text="", font=FONT, pady=30)

window.mainloop()