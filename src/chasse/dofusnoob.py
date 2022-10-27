from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import random
import logging
import re

SITE_URL = 'https://www.dofuspourlesnoobs.com/resolution-de-chasse-aux-tresors.html'
X_PATH = '//input[@id=\'huntposx\']'
Y_PATH = '//input[@id=\'huntposy\']'
D_CLASS = {
    "up": 'huntupwards',
    "down": 'huntdownwards',
    "left": 'huntleft',
    "right": 'huntright'
}   

class DofusNoob:
    """
    Class to load and interact with dofusnoob
    """

    def __init__(self):
        self.open()
        
    def open(self):
        capabilities = DesiredCapabilities.CHROME
        capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
        options = webdriver.ChromeOptions()
        options.add_argument('window-size=1920,1080')
        options.add_experimental_option("excludeSwitches", ['enable-logging'])

        self.driver = Chrome(options=options,desired_capabilities=capabilities)
        self.driver.minimize_window()
        self.wait = WebDriverWait(self.driver, 2)
        self.driver.get(SITE_URL)
        self.driver.find_element(By.XPATH, "//button[@mode=\'primary\']").click()

    @staticmethod
    def clear_and_set_field(element, value):
        """
        Clears the field element.
        """
        element.send_keys(Keys.CONTROL + 'a')
        time.sleep(0.1+random.random()*0.3)
        element.send_keys(Keys.BACK_SPACE)
        time.sleep(0.1+random.random()*0.3)
        element.send_keys(value)
        
    def get_hint(self, x, y, d, hint):
        """
        Get the elements in a dirtection from a position.
        """
        #set x y
        DofusNoob.clear_and_set_field(self.driver.find_element(By.XPATH, X_PATH), x)
        time.sleep(0.1+random.random())
        DofusNoob.clear_and_set_field(self.driver.find_element(By.XPATH, Y_PATH), y)
        
        #direction
        self.driver.find_element(By.XPATH, f"//label[@for=\'{D_CLASS[d]}\']").click()
        time.sleep(0.5)
        
        #select hint
        try:
            self.driver.find_element(By.XPATH, f"//option[not(@disabled) and contains(text(),'{hint}')]").click()
        except NoSuchElementException:
            logging.info(f'hint : {hint}, not found')
            return None
        
        time.sleep(0.5+random.random()*0.5)
        
        #click on submit
        self.driver.find_element(By.ID, "hunt-elt3").click()
        
        time.sleep(0.3+random.random()*0.3)
        
        #get result
        coord = self.driver.find_element(By.ID, "hunt-result-coord").text
        x,y = re.findall("\[(-?\d+),(-?\d+)\]",coord)[0]
        
        return (int(x),int(y))
        
        
        
        
        