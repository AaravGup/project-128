from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
import pandas as pd
import requests

page = requests.get()

URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs/"

browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(URL)
page = requests.get()

DwarfTables = soup.find("table", attrs={"class", "wikitable"})
tdRows = []
trTags = DwarfTables.find_all("tr")