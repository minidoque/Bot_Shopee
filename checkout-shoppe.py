import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

login_qr = "https://shopee.co.id/buyer/login/qr?next=https%3A%2F%2Fshopee.co.id%2F"  #url login via QR
product_name = "POLICE-Kemeja-Regular-Fit-Pria-621060774-Biru-i.56529142.6052840877" #Product url
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
        total_second = minutes * 60 + seconds - 1
        while total_second:
            mins, secs = divmod(total_second, 60)
            print(f'{mins:02d}:{secs:02d}', end='\r')
            time.sleep(1)
            total_second -= 1


class CheckOutBot(PrepareBot):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.manage().window().fullscreen()              #open the browser
        self.driver.get(flash_sale)                             #get the url from flashsale and search it

    def addProduct(self):
        # selectColor = self.driver.find_element_by_xpath(
        #     '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[5]/div/div[1]/div/button'     
        #     ).click()
        selectModel = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[1]/div/button[1]'
            ).click()
        add_to_cart = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]'
            ).click()
    
    def getProduct(self):
        time.sleep(5)
        checkout = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[3]/div[2]/div[7]/div[5]/button'
            ).click()
        time.sleep(5)
        make_order = self.driver.find_element_by_xpath(button_with_coin).click()


if __name__ == "__main__":
    checkOutBot = CheckOutBot()
    prepareBot = PrepareBot()

    prepareBot.countdownTimer()
    checkOutBot.addProduct()

    checkOutBot.getProduct()
    time.sleep(60)
