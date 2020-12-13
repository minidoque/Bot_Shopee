import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

login_qr = "https://shopee.co.id/buyer/login/qr?next=https%3A%2F%2Fshopee.co.id%2F"
product_name = "Apple-iPhone-11-Pro-512GB-Midnight-Green-i.255563049.6435648695"
flash_sale = login_qr + product_name

class PrepareBot:
    def prepare(self):
        self.driver = webdriver.Chrome()
        self.driver.get(flash_sale)
        checkOutBot = CheckOutBot()

    def countdownTimer(self):
        target_m = 59
        target_s = 60
        current_m = time.strftime("%M")
        current_s = time.strftime("%S")
        minutes = target_m - int(current_m)
        seconds = target_s - int(current_s)
        total_second = minutes * 60 + seconds - 1
        while total_second:
            mins, secs = divmod(total_second, 60)
            print(f'{mins:02d}:{secs:02d}', end='\r')
            time.sleep(1)
            total_second -= 1
        checkOutBot.addProduct()

    


class CheckOutBot(PrepareBot):
    def addProduct(self):
        # selectColor = self.driver.find_element_by_xpath(
        #     '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[5]/div/div[1]/div/button'
        #     ).click()
        # selectModel = self.driver.find_element_by_xpath(
        #     '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[3]/div/div[1]/div/button[4]'
        #     ).click()
        add_to_cart = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]'
            ).click()
    
    def getProduct(self):
        checkout = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button'
            ).click()
        time.sleep(6)
        make_order = self.driver.find_elements_by_class_name(
            '.stardust-button stardust-button--primary stardust-button--large _22Ktrb'
            ).click()   




if __name__ == "__main__":
    prepareBot = PrepareBot()
    prepareBot.prepare()
    prepareBot.countdownTimer()

    time.sleep(5)
    
    checkOutBot.getProduct()
    time.sleep(60)
    

    
