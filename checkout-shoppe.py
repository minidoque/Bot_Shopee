import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

flashSale = "https://shopee.co.id/buyer/login/qr?next=https%3A%2F%2Fshopee.co.id%2FApple-iPhone-11-Pro-512GB-Midnight-Green-i.255563049.6435648695"
testProduct = "https://shopee.co.id/buyer/login/qr?next=https%3A%2F%2Fshopee.co.id%2FConverse-70s-Black-Egrete-i.13080351.1902594721"

class CheckOutBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(flashSale)

    def addProduct(self):
        # selectColor = self.driver.find_element_by_xpath(
        #     '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[5]/div/div[1]/div/button'
        #     ).click()
        # selectModel = self.driver.find_element_by_xpath(
        #     '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[3]/div/div[1]/div/button[4]'
        #     ).click()
        addToCart = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]'
            ).click()
    
    def getProduct(self):
        checkout = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button'
            ).click()
        time.sleep(6)
        makeOrder = self.driver.find_elements_by_class_name(
            '.stardust-button stardust-button--primary stardust-button--large _22Ktrb'
            ).click()   


def countdownTimer():
    total_second = M * 60 + S - 1
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{mins:02d}:{secs:02d}', end='\r')
        time.sleep(1)
        total_second -= 1
    checkOutBot.addProduct()


if __name__ == "__main__":
    checkOutBot = CheckOutBot()

    currentM = time.strftime("%M")
    currentS = time.strftime("%S")

    targetM = 59
    targetS = 60

    M = targetM - int(currentM)
    S = targetS - int(currentS)

    countdownTimer()
    time.sleep(5)
    checkOutBot.getProduct()
    time.sleep(60)
    

    
