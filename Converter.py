#Предполагается вызывать Converter.main с переданным путем к .pdf из других файлов
import tabula
import sqlite3


def main(file):
    conn=sqlite3.connect('database.db')
    cur=conn.cursor()
    file='files/'+file

    groups=[]
    table=tabula.read_pdf(file, pages='all', pandas_options={'header':None})
    for i in range(len(table)):
        df=table[i].replace('\r','\n', regex=True)
        print(df)
        
        for j in range(len(df.columns)):
            groups.append(df[j].loc[0])
        #groups=groups[1:]
    print(groups)
    

main('02.10.pdf')
#Предстоит много работы с сортировкой информации из таблиц
#Разобраться с датафреймами pandas