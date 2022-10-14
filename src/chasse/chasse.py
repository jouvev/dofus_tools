from seleniumrequests import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests as req
import time

PARAMS = {'x':-1,'y':-1,'direction':6,'$limit':50,'lang':"fr"}

webdriver = Chrome()
response = webdriver.request('GET', 'https://www.google.com/')
print(response)
time.sleep(3)
webdriver.quit()


"""elem = driver.find_element(By.XPATH, "//input[@placeholder=\"X\"]")
elem.send_keys("-2")
elem = driver.find_element(By.XPATH, "//input[@placeholder=\"Y\"]")
elem.send_keys("-2")
elem = driver.find_element(By.XPATH, "//i[contains(@class,\"arrow-up\")]/..")
elem.click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//i[contains(@class,\"dropdown\")]/../..")))
elem = driver.find_element(By.XPATH, "//i[contains(@class,\"dropdown\")]/../..")
elem.click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class=\"q-item__label\"]")))
elem = driver.find_elements(By.XPATH, "//div[@class=\"q-item__label\"]")
print([e.text for e in elem])
elem[0].click()"""

"""URL = "https://api.dofusdb.fr/treasure-hunt"

PARAMS = {'x':-1,'y':-1,'direction':6,'$limit':50,'lang':"fr"}
o = {"origin":"https://dofusdb.fr","referer":"https://dofusdb.fr/","token":""}

h1 = {"Access-Control-Request-Headers":"token","origin":"https://dofusdb.fr","referer":"https://dofusdb.fr/"}
r = req.options(url = URL, params = PARAMS, headers = h1)
print("req 1",r)
print(r.headers)
print(r.text)

r = req.get(url = URL, params = PARAMS,headers=o)
print("req 2",r)
print(r.text)
data = r.json()

print(data)"""