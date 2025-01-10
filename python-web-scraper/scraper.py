from selenium import webdriver

website = 'https://hsmo.org/adopt/'
path = 'C:\Users\erins\Chromedriver\chromedriver-win64'
driver = webdriver.Chrome(path)
driver.get(website)