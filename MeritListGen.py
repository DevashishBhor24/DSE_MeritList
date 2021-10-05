from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import requests
import SeatListGen
import InputFile
df=pd.DataFrame(columns=['SeatNo','EnrollmentNo','Name','AggPer','Branch','Main Group','Sub Group'])

file=open('Subject_Codes.txt','r')
Branches={}
for i in file:
    if i not in Branches:
        Branches[i[11:-1]]=[i[:2],i[3:5],i[6:10]]

line_no=0

for seatno in SeatListGen.Seatlist:
    # seatno=int(seatno.strip())
    link1=InputFile.TakeInput.ResultUrl1+str(seatno)[:2]+"/"+str(seatno)+InputFile.TakeInput.ResultUrl2
    page = requests.get(link1,timeout=20.0)
    if page.status_code==200:
        soup = bs(page.content, features="html.parser") #html document
        percentage=soup.select('table')[2].select('tr')[4].select('td')[2].text
        EnrollmentNo=soup.select('table')[0].select('tr')[1].select('td')[1].text
        Name=soup.select('table')[0].select('tr')[0].select('td')[1].text
        Branch=soup.select('table')[0].select('tr')[2].select('td')[1].text
        groupcodes=(Branches[Branch.strip()[11:]] if Branch.strip()[11:]  in Branches.keys() else [Branch,'NA','NA'])
        df.loc[seatno]=[seatno,EnrollmentNo,Name,percentage, groupcodes[0],groupcodes[1],groupcodes[2]]
        print(seatno,percentage.ljust(6),EnrollmentNo.ljust(18),Name.ljust(30), groupcodes[0],groupcodes[1],groupcodes[2])
        line_no=line_no+1

    if line_no==10:
        time.sleep(8.0)
        line_no=0
        
df.to_excel('Meritlist.xlsx')
print("Done!!!")
