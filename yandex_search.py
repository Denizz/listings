from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from seo_walker import SeoWalker
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

        self.search_name_parts(np1, 1)

    def search_name_parts(self, np1, page):

        driver = self.driver
        driver.find_elements_by_xpath("//a[starts-with(@class, 'link link_ajax_yes link_theme_normal pager__item pager_')]")[page - 1].click()

        print("Page number " + str(page) + "clicked!")

        time.sleep(10)
        links = driver.find_elements_by_xpath("//a[starts-with(@class, 'link link_outer_yes')]")
        self.get_link(links, np1, page)



    def get_link(self, links, np1, page):
        url_tmp = []

        for i in range(0, len(links)):
            if re.search(np1, links[i].get_attribute("href")):
                url_tmp.append(links[i].get_attribute("href"))
                self.walk_in_page(links[i].get_attribute("href"))
                break

            else:
                print(links[i].get_attribute("href"))

        if len(url_tmp) == 0:
            page += 1
            self.search_name_parts(np1, page)




    def walk_in_page(self, url):
        driver = self.driver
        driver.get(url)
        print("I am inside of!" + url)
        sw = SeoWalker()
        sw.walk(url, 10)
        driver.close()


ns = YandexSearcher()
ns.search( "страна мам", r"blog.tr(.*)d.ru") #(.*) вместо неизвестных символов
