from helium import *
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

url = 'https://www.needypaws.org/animals/list'
browser = start_chrome(url, headless=False)


time.sleep(5)


soup = BeautifulSoup(browser.page_source, 'html.parser')


kill_browser()

dog_list = []
rows = soup.find_all('tr')

for row in rows:
    columns = row.find_all('td', class_='portalTableValue')
    
    if len(columns) >= 3:
        name = columns[0].text.strip()
        breed = re.sub(r"^Dog\s*-\s*", "", columns[1].text.strip())  # Remove "Dog - "
        gender = columns[2].text.strip()
        
        dog_list.append([name, breed, gender])


df = pd.DataFrame(dog_list, columns=['Name', 'Breed', 'Gender'])


df.to_csv("dog_listings_cleaned.csv", index=False)
print(df.head())
