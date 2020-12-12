import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

flashSale = "https://shopee.co.id/buyer/login/qr?next=https%3A%2F%2Fshopee.co.id%2FLEGO-Creator-31092-Helicopter-Adventure-(114-Buah)-Mainan-Anak-Petualangan-Helikopter-(6-Tahun-)-i.312618972.6855892346"
testProduct = "https://shopee.co.id/buyer/login/qr?next=https%3A%2F%2Fshopee.co.id%2FConverse-70s-Black-Egrete-i.13080351.1902594721"


def countdownTimer(start_minute, start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{mins:02d}:{secs:02d}', end='\r')
        time.sleep(0.92)
        total_second -= 1
    checkOutBot.addProduct()

class CheckOutBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(flashSale)

    def addProduct(self):
        addToCart = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]'
            ).click()
    
    def getProduct(self):
        time.sleep(5)
        checkout = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[3]/div[2]/div[7]/div[5]/button'
            ).click()
        time.sleep(6)
        makeOrder = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[3]/div[4]/div[2]/div[14]/button'
            ).click()


if __name__ == "__main__":
    checkOutBot = CheckOutBot()

    countdownTimer(3,10)
    time.sleep(1)
    checkOutBot.getProduct()
    time.sleep(60)
    

    
