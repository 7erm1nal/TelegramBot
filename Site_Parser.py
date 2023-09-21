import os
import requests
from bs4 import BeautifulSoup
import datetime

#Функция определения времени
#На вход подается реквест (год, месяц, день, час, завтра)  На выход нужная строка
def current_date(req=str):                
    dt=datetime.datetime.now()
    if req=='year':    
        return dt.strftime("%Y")
    if req=='tomorrow':
        tomorrow=datetime.datetime.today() + datetime.timedelta(days=1)
        return tomorrow.strftime("%d") 
    if req=='month':
        return dt.strftime("%m")
    if req=='hour':
        return dt.strftime("%H")
    if req == 'day':
        return dt.strftime("%d")

#Функция на случай расписания на пт-сб 
def weekend():
    pass


#Функция скачивания pdf файла с указанного url
def parse(url=str):
    req=requests.get(url)
    soup = BeautifulSoup(req.text)
    links=soup.find_all('a')
    for link in links:
        if('.pdf' in link.get('href', []) and current_date('tomorrow') in link.get('href', [])):
            #Чертовски перегруженное ветвление:
            #Первая проверка на .pdf в ссылке + наличие завтрашней даты
            #Вторая проверка на наличие завтрашней даты в нужном месте ссылки(тут \/ )
            #От последнего слеша до месяца+.pdf  /ipek/SiteAssets/01/rz/2023/09/22,23.09.pdf
            path=link.get('href', [])
            if(current_date('tomorrow') in path[path.rindex('/'):path.index(current_date('month')+'.pdf')]):
                i=path[path.rindex('/'):path.index('.'+current_date('month')+'.pdf')]+'.'+current_date('month')+".pdf"
                i=i[1::]                        #Название скачиваемого файла
                print("Downloading file: ", i)
                req = requests.get("https://ciur.ru"+link.get('href'))
                pdf = open(i, 'wb')
                pdf.write(req.content)
                pdf.close()
                os.rename(i, "files/"+i)        #Перенос в папку files
                print("File ", i, " downloaded")
                if ',' in i:
                    weekend()                   #Если название файла имеет запятую
                                                #значит в нем содержится расписание на пт-сб
                                                #перенаправить в функцию "Выходные"


url = "https://ciur.ru/ipek/SiteAssets/01/rz/"+current_date("year")+"/"+current_date("month")+"/"  #Ипэк, папка с файлами на месяц 
#url = "https://ciur.ru/ipek/DocLib61/Forms/AllItems.aspx"                                          #Ипэк, вкладка с расписанием на сайте

parse(url)