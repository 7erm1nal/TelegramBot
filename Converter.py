import PyPDF2

file="files/21.09.pdf"
with open(file, 'rb') as pdffile:
    pdf=PyPDF2.PdfReader(pdffile)
    page=pdf.pages[0]
    print(page.extract_text())

#Имею представление как делить инфу на ячейки таблицы pdf
#И совершенно не имею понятия как раскидывать их по группам
#
#Хотелось бы заиметь рабочую библиотеку на питон
#tabula/camelot/fitz выдают ошибки либо не работают