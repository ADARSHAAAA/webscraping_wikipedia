# -*- coding: utf-8 -*-
"""webscraping_wikipedia.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xc37V2l5OVafkaxxg5K_lOPXWg8O1dIf
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

webpage=requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population').text

soup=BeautifulSoup(webpage,'lxml')

countries = []
population = []
percent = []
date = []

for row in soup.find_all('tr'):
    cells = row.find_all('td')


    if len(cells) > 1:
      country = cells[1].text.strip()
      populations = cells[2].text.strip()
      per = cells[3].text.strip()
      dte = cells[4].text.strip()

      if "World" in country or country == "":
          continue
      countries.append(country)
      population.append(populations)
      percent.append(per)
      date.append(dte)

df=pd.DataFrame({'country':countries,
   'population':population,
   'percent':percent,
   'date':date,
   })

df.head(210)

