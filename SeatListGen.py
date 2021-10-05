from bs4 import BeautifulSoup as bs
from typing import Final
import time
import requests
import InputFile

Seatlist=[]
InputTake=InputFile.TakeInput()
InputTake.FirstInput()
line_no=0
for seatno in range(InputTake.SeatRangeStart,InputTake.SeatRangeEnd):
    link1=InputTake.ResultUrl1+str(seatno)[:2]+"/"+str(seatno)+InputTake.ResultUrl2
    page = requests.get(link1)
    try:
        if page.status_code==200:
            soup = bs(page.content, features="html.parser") #html document
            if len(soup.select('table')[2].select('tr'))==6 :
                if  soup.select('table')[0].select('tr')[2].select('td')[1].text != 'Diploma In Pharmacy':
                    Seatlist.append(seatno)
                    line_no=line_no+1 
    except IndexError:
        continue

    finally:
        if line_no==10:
            time.sleep(8.0)
            line_no=0