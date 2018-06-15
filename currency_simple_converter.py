# Program gets currency exchange rates using www.xe.com/currencyconverter
# the exchange rate from one currency to another will be written to terminal

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class CurrencyExchange():

    def test(self,curr1, curr2):
        base_url = "https://www.xe.com/currencyconverter/"
        driver = webdriver.Firefox()
        #driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        from_curr = driver.find_element(By.ID, "from")
        from_curr.send_keys(curr1)
        time.sleep(2)
        from_curr.send_keys(u'\ue007')

        to_curr = driver.find_element(By.ID, "to")
        to_curr.send_keys(curr2)
        time.sleep(2)
        to_curr.send_keys(u'\ue007')

        when = driver.find_element(By.ID,"ucc_go_btn_svg")
        when.click()
        time.sleep(2)

        checkin = driver.find_element(By.XPATH, "(//span[@class ='uccResultAmount'])").get_attribute("innerHTML")
        print(str(checkin))
        driver.close()

ff = CurrencyExchange()
ff.test("EUR","TRY")
