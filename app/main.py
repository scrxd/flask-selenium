import os
from flask import Flask
from selenium import webdriver

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
        #driver.get('https://kartaca.com')
        driver.get('https://www.kap.org.tr/tr/bildirim-sorgu?member=4028e4a1413b7ef401413bc2251e0047')
        elements = driver.find_elements_by_class_name('w-clearfix.notifications-row')
        return str(elements.__len__())
        #return "test test"
    finally:
        print("sfdsf")
