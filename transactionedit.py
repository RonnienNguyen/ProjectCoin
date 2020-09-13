from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions


chromeOptions = ChromeOptions()

chromeOptions.add_extension('hello.crx')

driver = webdriver.Chrome(
    'D:\Source code Python\Coin App\chromedriver.exe', options=chromeOptions)

driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password/import-with-seed-phrase")

searchpass

search = driver.find_element_by_id("password")
search.send_keys(searchpass)
search.send_keys(Keys.RETURN)

search1 = driver.find_element_by_id("confirm-password")
search1.send_keys(searchpasscf)
search1.send_keys(Keys.RETURN)


search0 = driver.find_element_by_class_name("MuiInputBase-input")
search0.send_keys(
    "praise transfer smart review game way top era rival unveil suit pelican")
search0.send_keys(Keys.RETURN)


botton2 = driver.find_element_by_class_name("first-time-flow__checkbox")
botton2.click()

botton = driver.find_element_by_class_name("first-time-flow__terms")
botton.click()

bottnxt = driver.find_element_by_class_name("first-time-flow__button")
bottnxt.click()

time.sleep(2)

bttk = driver.find_element_by_class_name("first-time-flow__button")
bttk.click()

time.sleep(2)
bttsend = driver.find_element_by_class_name("btn-secondary")
bttsend.click()

time.sleep(2)
bttidaddress = driver.find_element_by_class_name("ens-input__wrapper__input")
bttidaddress.send_keys("0x51923d87c096dfEF7962b97A9c315e147302e1e9")
bttidaddress.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

# ethamount = driver.find_element_by_class_name("unit-input__input")
# ethamount.send_keys('50')
# ethamount.send_keys(Keys.RETURN)
