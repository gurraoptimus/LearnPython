import padnas as pd
import openpyxl
import requests as re
from bs4 import BeautifulSoup as bs

data = re.get("pass")
data_parse = bs(data.content, "xml")

data_find = data_parse.find_all("loc")
for item in data_find:
    data_temp = re.get(item.contents[0])
    data_temp_parse = bs(data_temp.content, "html.parser")
    text = data_temp_parse.title.text
    if "pass" in text.lower():
        print(text)