from pdf2docx import Converter

pdf_path = input("Enter your PDf path : ")
docx_file_name = input("Enter your saving docx file name : ")
docx_path = "C:/Users/MUH TOLGA/Desktop/" + docx_file_name

cv = Converter(pdf_path)
cv.convert(docx_path)
cv.close()