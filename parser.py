import requests
from bs4 import BeautifulSoup


site = "https://www.ph4.ru/eng_irregular.php?ts=&al=a"

requests.get(site)
parser = BeautifulSoup()