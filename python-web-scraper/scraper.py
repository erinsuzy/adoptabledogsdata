from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = 'https://hsmo.org/adopt/'
path = r'C:\Users\erins\Chromedriver\chromedriver-win64\chromedriver.exe'
service = Service(path)
driver = webdriver.Chrome(service=service)
driver.get(website)