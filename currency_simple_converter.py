from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AirbnbExercise1():

    def test(self,curr1, curr2):
        base_url = "https://www.xe.com/currencyconverter/"
        driver = webdriver.Firefox()
        #driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        # Elements and design has changed on Airbnb website after the lecture was made
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

ff = AirbnbExercise1()
ff.test("TRY","RUB")
