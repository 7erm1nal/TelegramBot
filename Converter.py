#Предполагается вызывать Converter.main с переданным путем к .pdf из других файлов
import tabula
import sqlite3
def main(file):
    conn=sqlite3.connect('database.db')
    cur=conn.cursor()

    file='files/'+file
    table=tabula.read_pdf(file, pages=1)
    groups=table[0]
    print(groups)


main('02.10.pdf')
#Предстоит много работы с сортировкой информации из таблиц
#Разобраться с датафреймами pandas
