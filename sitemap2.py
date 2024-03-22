import pandas as pd
import openpyxl
import requests as re
from bs4 import BeautifulSoup as bs

data = re.get("https://gurraoptimus.se/sitemap.xml")
data_new = bs(data.content, "xml")
print(data_new)