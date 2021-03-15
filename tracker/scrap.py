import builtwith
import whois
import re
import urllib.request
import requests
from bs4 import BeautifulSoup

from lxml import html 

r = requests.get('https://facebook.com/')
soup = BeautifulSoup(r.text, 'lxml')
url = 'https://authoraditiagarwal.com/leadershipmanagement/'
path = '//*[@id="panel-836-0-0-1"]/div/div/p[1]'
response = requests.get(url)
byte_string = response.content
source_code = html.fromstring(byte_string)
tree = source_code.xpath(path)
print(tree[0].text_content()) 


