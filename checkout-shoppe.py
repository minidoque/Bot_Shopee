import datetime, time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = Options()
options.page_load_strategy = 'eager'

login_qr = "https://shopee.co.id/buyer/login/qr?next=https%3A%2F%2Fshopee.co.id%2F"  #url login via QR
product_name = "Samsung-Galaxy-S20-FE-256-GB-Cloud-Orange-i.52635036.6259445668"                                        #Product url
flash_sale = login_qr + product_name                                                 #Destination url , from qr url and product url 

class ShopBot():
    def __init__(self): 
        self.driver = webdriver.Chrome(options = options)
        self.driver.maximize_window()
        self.driver.get(flash_sale)               #open the browser and get the url from flashsale and search it

    def countdownTimer(self):                           #for countdown to get the flash sale
        today = datetime.datetime.now()
        delta = (datetime.datetime(2021, 3, 3, 1, 0, 0) -  today).seconds
        while delta:
            print(str(delta))
            time.sleep(1)
            today = datetime.datetime.now()
            delta = (datetime.datetime(2021, 3, 3, 1, 0, 0) -  today).seconds
        print('NOW')
        self.driver.refresh()

    def addProduct(self):
        self.driver.implicitly_wait(5)

        add_to_cart = self.driver.find_element_by_class_name("btn-solid-primary.btn--l").click()
    
    def getProduct(self):
        self.driver.implicitly_wait(10)

        checkout = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.CLASS_NAME, "shopee-button-solid.shopee-button-solid--primary")
                    ))
        checkout.send_keys(Keys.SPACE)

        self.driver.implicitly_wait(6)

        bank_transfer = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[1]/div[2]/span[2]")
                    )).click
        #bank_transfer.send_keys(Keys.SPACE)

        bni = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div/div/div[2]")
                    )).click
        #bni.send_keys(Keys.ENTER)

        make_order = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.CLASS_NAME, "stardust-button.stardust-button--primary")
                    ))
        make_order.send_keys(Keys.ENTER) 

if __name__ == "__main__":
    ShopBot = ShopBot()
    ShopBot.countdownTimer()
    ShopBot.addProduct()
    ShopBot.getProduct()
    time.sleep(5)
