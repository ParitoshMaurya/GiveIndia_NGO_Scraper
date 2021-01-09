import requests
from bs4 import BeautifulSoup as bs
import json

url='https://www.giveindia.org/certified-indian-ngos'
r=requests.get(url)
htmlCon=r.content
soup=bs(htmlCon,'html.parser')


table=soup.find('table',class_='jsx-697282504 certified-ngo-table')
all_tr=table.find_all('tr',class_='jsx-697282504')
f=open('scraped_data.json','w+')

for i in range(1,len(all_tr)):
    elm=all_tr[i]
    name_of_NGO=elm.td.div.div.text
    all_td=elm.find_all('td',class_='jsx-697282504')
    cause_of_NO=all_td[1].text
    State=all_td[2].text
    json.dump({'Details of NGO '+str(i):{'Name': name_of_NGO ,'Cause':cause_of_NO ,'State':State}},f,indent=2)

f.close()



