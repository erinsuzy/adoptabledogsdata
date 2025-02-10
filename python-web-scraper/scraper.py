from helium import *
from bs4 import BeautifulSoup
import pandas as pd
import time


url = 'https://www.needypaws.org/animals/list'
browser = start_chrome(url, headless=False)


time.sleep(15)  


soup = BeautifulSoup(browser.page_source, 'html.parser')

kill_browser()


rows = soup.find_all('tr') 

dog_list = []


for row in rows:
    columns = row.find_all('td', class_='portalTableValue')
    
    if len(columns) >= 3:  
        name = columns[0].text.strip()  
        breed = columns[1].text.strip()  
        gender = columns[2].text.strip()  
        
        dog_list.append([name, breed, gender])


df = pd.DataFrame(dog_list, columns=['Name', 'Breed', 'Gender'])


df.to_csv("dog_listings.csv", index=False)


print(df.head())
