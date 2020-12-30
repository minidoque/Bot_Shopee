import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.page_load_strategy = 'eager'

login_qr = "https://shopee.co.id/buyer/login/qr?next=https%3A%2F%2Fshopee.co.id%2F"  #url login via QR
product_name = "Fladeo-E20-LDS257-2RA-Sandal-For-Ladies-Teplek-Style--i.30964028.6832819136" #Product url
flash_sale = login_qr + product_name                                                 #Destination url , from qr url and product url 

button_without_coin = '//*[@id="main"]/div/div[2]/div[3]/div[4]/div[2]/div[9]/button'
button_with_coin = '//*[@id="main"]/div/div[2]/div[3]/div[4]/div[2]/div[12]/button'


class PrepareBot:
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
            time.sleep(1)
            total_second -= 1


class CheckOutBot(PrepareBot):
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(flash_sale)               #open the browser and get the url from flashsale and search it

    def addProduct(self):
        self.driver.implicitly_wait(5)
        selectColor = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[3]/div/div[1]/div/button[1]'     
            ).click()
        selectModel = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[3]/div/div[2]/div/button[3]'
            ).click()
        add_to_cart = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]'
            ).click()
    
    def getProduct(self):
        self.driver.implicitly_wait(10)
        checkout = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[3]/div[2]/div[7]/div[5]/button'
            ).click()
        make_order = self.driver.find_element_by_xpath(button_with_coin).click()


if __name__ == "__main__":
    checkOutBot = CheckOutBot()
    prepareBot = PrepareBot()

    prepareBot.countdownTimer()

    
    checkOutBot.addProduct()
    checkOutBot.getProduct()
    time.sleep(60)
