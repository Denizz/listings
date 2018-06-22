from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re


class YandexSearcher():

    def search(self, phrase, np1):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.yandex.ru")

        input_field = self.driver.find_element_by_id("text")
        input_field.send_keys(phrase)
        input_field.send_keys(u'\ue007')

        self.driver.implicitly_wait(10)
        print(" opened")

        self.search_name_parts(np1)

    def search_name_parts(self, np1):
        driver = self.driver
        url_tmp = []
        time.sleep(10)
        links = driver.find_elements_by_xpath("//a[starts-with(@class, 'link link_outer_yes')]")

        for i in range(0,len(links)):
            if re.search(np1, links[i].get_attribute("href")):
                url_tmp.append(links[i].get_attribute("href"))
                self.walk_in_page(links[i].get_attribute("href"))
                break

            else:
                print(links[i].get_attribute("href"))

    def walk_in_page(self, url):
        driver = self.driver
        driver.get(url)
        print("I am inside of!" + url)
        driver.close()


ns = YandexSearcher()
ns.search( "Поразительный дизайн​", r"di(.*)om.ru") #(.*) вместо неизвестных символов
