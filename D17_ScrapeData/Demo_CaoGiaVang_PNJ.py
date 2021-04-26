from bs4 import BeautifulSoup
import requests
import schedule
import time


def scrape_pnj_price():
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
    # Process data nhận được


schedule.every(7).seconds.do(scrape_pnj_price)

while True: 
    schedule.run_pending()
    time.sleep(1)