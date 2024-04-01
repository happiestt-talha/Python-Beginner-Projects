import pdfplumber
path = "D:\Timetable3.pdf"
with pdfplumber.open(path) as pdf:
    for page in pdf.pages:
        print(page.extract_text())
