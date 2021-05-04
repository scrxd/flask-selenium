import os
from selenium import webdriver
import json
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-sh-usage")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
# driver.get('https://www.kap.org.tr/tr/')
#driver.get('https://www.kap.org.tr/tr/bildirim-sorgu?member=4028e4a1413b7ef401413bc2251e0047')
driver.get('https://www.kap.org.tr/tr/bildirim-sorgu?member=4028e4a140f2ed7201411682b0cb05c6')
# driver.get('https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/default.aspx')
time.sleep(0.1)

elements = driver.find_elements_by_class_name('w-clearfix.notifications-row')

kaplar = []

for e in elements:
    column = e.find_elements_by_class_name('notifications-column')
    # print('C_LEN: ' + column.__len__().__str__())
    # print('')
    if column.__len__() == 11:
        # for c in column:
        #     print('CT: ' + c.text)

        sayi = column[0].text
        tarih = column[1].text
        kod = column[2].text
        sirket = column[3].text
        tip = column[4].text
        konu = column[5].text
        ozet = column[6].text
        ilgili = column[7].text
        yil = column[8].text
        periyot = column[9].text

        # print('sayi: ' + sayi)
        # print('tarih: ' + tarih)
        # print('kod: ' + kod)
        # print('sirket: ' + sirket)
        # print('tip: ' + tip)
        # print('konu: ' + konu)
        # print('ozet: ' + ozet)
        # print('ilgili: ' + ilgili)
        # print('yil: ' + yil)
        # print('periyot: ' + periyot)
        # print('')

        kap = {
            'sayi': sayi,
            'tarih': tarih,
            'kod': kod,
            'sirket': sirket,
            'tip': tip,
            'konu': konu,
            'ozet': ozet,
            'ilgili': ilgili,
            'yil': yil,
            'periyot': periyot
        }

        kaplar.append(kap)

kaplar_json = json.dumps(kaplar)

print(kaplar_json)

time.sleep(0.1)
driver.close()
print("bitti")