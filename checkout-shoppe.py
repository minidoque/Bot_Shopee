import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = EdgeOptions()
options.use_chromium = True
options.page_load_strategy = 'eager'

login_qr = "https://shopee.co.id/buyer/login/qr?next=https%3A%2F%2Fshopee.co.id%2F"  #url login via QR
product_name = "Coolant-Lychee-350-ml-x-4-Pcs-i.78892667.7539221087"                                        #Product url
flash_sale = login_qr + product_name                                                 #Destination url , from qr url and product url 

button_without_coin = '//*[@id="main"]/div/div[2]/div[3]/div[4]/div[2]/div[9]/button'
button_with_coin = '//*[@id="main"]/div/div[2]/div[3]/div[4]/div[2]/div[12]/button'


class ShopBot():
    def __init__(self): 
        self.driver = Edge(options = options)
        self.driver.maximize_window()
        self.driver.get('https://shopee.co.id/Coolant-Lychee-350-ml-x-4-Pcs-i.78892667.7539221087')               #open the browser and get the url from flashsale and search it

    def countdownTimer(self):                           #for countdown to get the flash sale
        target_m =4                                    #target minute the flash sale can click (minute - 1)
        target_s =60                                    #target seconds the flash sale can click                           
        current_m = time.strftime("%M")
        current_s = time.strftime("%S")
        minutes = target_m - int(current_m) - 1
        seconds = target_s - int(current_s)
        # total_second = minutes * 60 + seconds - 1
        total_second = 20
        while total_second:
            mins, secs = divmod(total_second, 60)
            print(f'{mins:02d}:{secs:02d}', end='\r')
            time.sleep(0.99)
            total_second -= 1
        self.driver.refresh()

    def addProduct(self):
        self.driver.implicitly_wait(30)

        add_to_cart = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]'
            ).click()
    
    def getProduct(self):
        self.driver.implicitly_wait(10)

        checkout = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[3]/div[2]/div[7]/div[5]/button')
                    ))
        checkout.click()

        make_order = self.driver.find_element_by_xpath(button_with_coin).click()


if __name__ == "__main__":
    ShopBot = ShopBot()

    ShopBot.countdownTimer()

    
    ShopBot.addProduct()
    # checkOutBot.getProduct()
    time.sleep(5)


    # selectColor = self.driver.find_element_by_xpath(
    #     '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[3]/div/div[1]/div/button[1]'     
    #     ).click()
    # selectModel = self.driver.find_element_by_xpath(
    #     '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[3]/div/div[2]/div/button[3]'
    #     ).click()
