import requests
from bs4 import BeautifulSoup

URL = 'https://www.pnj.com.vn/blog/gia-vang/'
page = requests.get(URL)
# print(page.text)

# .widget_ty_gia_gia_vang_widget --> next
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ty_gia_gia_vang_widget-2')
name_elems = results.find_all('td', class_='colorGrey')
price_in_elems = results.find_all('td', class_='price_in')
price_out_elems = results.find_all('td', class_='price_out')

print(results.prettify())
for name_elem in name_elems:
    print(name_elem, end='\n')
    print(name_elem.text.strip())