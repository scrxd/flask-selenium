import os
from flask import Flask
from selenium import webdriver
import json
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-sh-usage")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

app = Flask(__name__)

@app.route('/')
def index():
    try:
        kaplar = []
        driver.get('https://www.kap.org.tr/tr/bildirim-sorgu?member=4028e4a1413b7ef401413bc2251e0047')
        time.sleep(1)

        elements = driver.find_elements_by_class_name('w-clearfix.notifications-row')

        for i in range(2):
            column = elements[i].find_elements_by_class_name('notifications-column')
            if column.__len__() == 11:
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

        # json formatında dondurur
        response = app.response_class(
            response=json.dumps(kaplar),
            status=200,
            mimetype='application/json'
        )
        #print("driver.title")
        return response
        #return "title: " + driver.title
    finally:
        print("driver.quit()")
        driver.quit()
