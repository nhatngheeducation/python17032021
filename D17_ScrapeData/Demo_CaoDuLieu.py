from bs4 import BeautifulSoup
import requests
import schedule
import time
from datetime import datetime
import json



def tra_cuu_lich_mat_dien(pe):
    url = 'https://cskh.evnhcmc.vn/tracuu/ajax_thongTinCungCapDien_result'
    myobj = {
        'input_makh': pe,
        'tungay': '26/04/2021',
        'denngay': '03/05/2021'
    }
    x = requests.post(url, data=myobj, verify=False)
    print(x.text)


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


def call_function_schedule():
    schedule.every(7).seconds.do(scrape_pnj_price)

    while True:
        schedule.run_pending()
        time.sleep(1)

# scrape_pnj_price()
# tra_cuu_lich_mat_dien('PE04000246146')


def scrap_gold_price_pnj():
    URL = 'https://www.pnj.com.vn/blog/gia-vang/'
    page = requests.get(URL)
    # print(page.text)

    # .widget_ty_gia_gia_vang_widget --> next
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='ty_gia_gia_vang_widget-2')
    name_elems = results.find_all('td', class_='colorGrey')
    price_in_elems = results.find_all('td', class_='price_in')
    price_out_elems = results.find_all('td', class_='price_out')

    names = []
    prices_in = []
    prices_out = []

    for name_elem in name_elems:
        names.append(name_elem.text.strip())

    for pin in price_in_elems:
        data_process = pin.find_all('span', class_='fixW')
        if len(data_process) > 0:
            for item in data_process:
                prices_in.append(item.text)

    for pout in price_out_elems:
        data_process = pout.find_all('span', class_='fixW')
        if len(data_process) > 0:
            for item in data_process:
                prices_out.append(item.text)

    pnj_gold_price = []
    if len(names) == len(prices_in) and len(prices_in) == len(prices_out):
        for index in range(0, len(names)):
            pnj_gold_price.append({
                "name": names[index],
                "price_in": prices_in[index],
                "price_out": prices_out[index],
            })

        now = datetime.now()  # current date and time
        filename = r"data\pnj_" + now.strftime("%m_%d_%Y_%H_%M_%S") + ".json"
        with open(filename, "w", encoding="utf-8") as myfile:
            json.dump(pnj_gold_price, myfile, indent=4, ensure_ascii=False)


# Demo
# scrap_gold_price_pnj()