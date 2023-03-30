from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
import pandas as pd
import requests


START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars/"

browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

scraped_data = []

starTable = soup.find("table", attrs = {"class", "wikitable sortable jquery-tablesorter"})
table_body = starTable.find("tbody")
table_rows = table_body.find_all("tr")
for row in table_rows:
        table_cols = row.find_all("td")
        print(table_cols)
        temp_list = []
        for col_data in table_cols:
            #print(col_data.text)
            data = col_data.text.strip()
            print(data)
            temp_list.append(data)
        scraped_data.append(temp_list)
stars_data = []
for i in range(0,len(scraped_data)):
      stars_data.append([scraped_data[i][1], scraped_data[i][2], scraped_data[i][3], scraped_data[i][5], scraped_data[i][6], scraped_data[i][7]])
headers = ['Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity']
star_df_1 = pd.DataFrame(stars_data, columns = headers)
star_df_1.to_csv('scraped_data.csv', index = True, index_label= id)   

        
                