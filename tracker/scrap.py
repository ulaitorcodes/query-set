

import requests
from bs4 import BeautifulSoup
import csv
import json
r = requests.get('https://www.tutorialspoint.com/python_web_scraping/python_web_scraping_data_processing.htm')
soup = BeautifulSoup(r.text, 'lxml')
y = json.dumps(soup.title.text)
with open('JSONFile.txt', 'wt') as outfile:
   json.dump(y, outfile)