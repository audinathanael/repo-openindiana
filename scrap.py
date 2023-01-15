from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver= webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

names=[]
versions=[]
driver.get("https://pkg.openindiana.org/dev/en/catalog.shtml")

content = driver.page_source
soup= BeautifulSoup(content)
for a in soup.findAll("tbody"):
    name= a.find('a',attrs={'title':'Package Information Summary'})
    names.append(name.text)

    print(names)

