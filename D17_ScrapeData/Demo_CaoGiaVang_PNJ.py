from bs4 import BeautifulSoup
import requests
import schedule
import time


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


schedule.every(7).seconds.do(scrape_pnj_price)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

tra_cuu_lich_mat_dien('PE04000246146')