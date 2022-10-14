from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


class Browser:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://dofusdb.fr/fr/tools/treasure-hunt")
        
    def _set_pos(self,x,y):
        elem = self.driver.find_element(By.XPATH, "//input[@placeholder=\"X\"]")
        elem.send_keys(f"{x}")
        time.sleep(0.5)
        elem = self.driver.find_element(By.XPATH, "//input[@placeholder=\"Y\"]")
        elem.send_keys(f"{y}")
        
    def _set_dir(self,direction):
        direction = direction.lower()
        if(direction not in ["up","down","left","right"]):
            raise Exception("Not a direction")
        elem = self.driver.find_element(By.XPATH, "//i[contains(@class,\"arrow-"+direction+"\")]/..")
        elem.click()
        
    def _get_hints(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//i[contains(@class,\"dropdown\")]/../..")))
        self.driver.find_element(By.XPATH, "//i[contains(@class,\"dropdown\")]/../..").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class=\"q-item__label\"]")))
        elems = self.driver.find_elements(By.XPATH, "//div[@class=\"q-item__label\"]")
        return {e.text : e for e in elems}
    
    def resolve_treasure(self, x, y, direction, hint):
        self._set_pos(x, y)
        time.sleep(0.5)
        self._set_dir(direction)
        time.sleep(0.5)
        hints = self._get_hints()
        time.sleep(0.5)
        if(hint in hints):
            hints[hint].click()
        else:
            raise Exception(f"{hint} missing")
        elems = self.driver.find_elements(By.XPATH, "//i[contains(@class,\"arrow\") and contains(@class,\"text-secondary\")]/..")
        print("elems => ",elems[0].text)
        
    def quit(self):
        self.driver.quit()
        
if(__name__ == '__main__'):
    try :
        bro = Browser()
        x = random.randint(-2,10)
        y = random.randint(-2,10)
        dir = random.choice(["up","down","left","right"])
        bro.resolve_treasure(x,y,dir,"Framboisier")
    finally:
        input()
        bro.quit()
    