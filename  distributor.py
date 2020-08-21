import requests
from requests import get
from bs4 import BeautifulSoup

import pandas as pd  
import numpy as np 
from time import sleep
from random import randint
import csv
distributors = []
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'image/webp,*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Referer': 'https://st.tistatic.com/ver9235/css/jquery_ui.css',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers',
}
 
     
response = requests.get("https://www.getdistributors.com/distributors/search_action.html?keyword=&category_id=395&investment_range=&search=&mode=&investment_period=&state_name=&city_id_input=&city_id=&country_code=&state=&city=&dummy_isd_field=&city_nearest_branch=", headers=headers)
print(response) 
soup = BeautifulSoup(response.content, "html.parser")
     
des = soup.find_all('div',class_='beansClintBox')
     
for container in des:
        name1 = container.find('span', {'class':"title"})
        distributors.append(name1)
        # name2 = container.find('span',{'id':"title-101252"})
        # distributors.append(name2)
        print(name1)
 