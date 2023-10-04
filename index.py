import datetime
import Site_Parser

#Стартовый файл, запускающий остальные файлы по цепочке в нужное время
#Доработаю
def timer():

    url = "https://ciur.ru/ipek/SiteAssets/01/rz/"+Site_Parser.current_date("year")+"/"+Site_Parser.current_date("month")+"/"  #Ипэк, папка с файлами на месяц 
    #url = "https://ciur.ru/ipek/DocLib61/Forms/AllItems.aspx"                                                                  #Ипэк, вкладка с расписанием на сайте

    time_for_parse="17 30"
    while True:
        if datetime.datetime.now().strftime("%H %M")==time_for_parse:
            print('time')
            Site_Parser.parse(url)
            break



if __name__=='__main__':
    timer()
    