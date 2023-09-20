import os
import requests
from bs4 import BeautifulSoup
import datetime

#url = "https://ciur.ru/ipek/SiteAssets/01/rz/"+current_date("year")+"/"+current_date("month")+"/"  #Ипэк, папка с файлами на месяц 
url="https://ciur.ru/ipek/DocLib61/Forms/AllItems.aspx"                                             #Ипэк, вкладка с расписанием на сайте


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

#Функция скачивания pdf файла с указанного url
def parse(url=str):
    req=requests.get(url)
    soup = BeautifulSoup(req.text)
    links=soup.find_all('a')
    for link in links:
        if('.pdf' in link.get('href', [])) and (current_date('tomorrow') in link.get('href', [])): #Успешно парсит нужный файл
            i=current_date('tomorrow')+'.'+current_date('month')+".pdf"
            print("Downloading file: ", i)
            req = requests.get("https://ciur.ru"+link.get('href'))
            pdf = open(i, 'wb')
            pdf.write(req.content)
            pdf.close()
            os.rename(i, "files/"+i)
            print("File ", i, " downloaded")

parse(url)
