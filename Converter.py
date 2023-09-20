from PyPDF2 import PdfReader

reader = PdfReader("files/21.09.pdf")                 #Позже сделать динамическое изменение названия файла
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)