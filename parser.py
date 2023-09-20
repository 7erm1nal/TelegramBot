import requests
from bs4 import BeautifulSoup
import datetime


#Функция определения времени
#На вход подается реквест (год, месяц, день, час, завтра)
#На выход нужная строка
def current_date(req):                
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


def parse(url=str):
    req=requests.get(url)
    soup= BeautifulSoup(req.text)
    links=soup.find_all('a')
    i=0
    for link in links:
        if('.pdf' in link.get('href', [])):
            i+=1
            print("Downloading file: ", i)
            req = requests.get("https://ciur.ru"+link.get('href'))  #Ввести проверку на наличие нужных файлов
            pdf = open("pdf"+str(i)+".pdf", 'wb')                   #"pdf" изменить на дату в расписании
            pdf.write(req.content)
            pdf.close()
            print("File ", i, " downloaded")
    
    print("All PDF files downloaded") 



url = "https://ciur.ru/ipek/SiteAssets/01/rz/2023/09/" #Изменять ссылку каждый месяц и год
parse(url)
