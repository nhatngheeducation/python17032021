from bs4 import BeautifulSoup
import requests

pnjObj = requests.get("https://giavang.pnj.com.vn/")
textContent = pnjObj.text

soup = BeautifulSoup(textContent, features="html.parser")

tdgroups = soup.find_all('td')
data = []
for item in tdgroups:
    print(item.text)
    if item.get_attribute_list('align') == ['center'] and \
        item.get_attribute_list('valign') == ['middle']:
        data.append(item.text)

print(data)
