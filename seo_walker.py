# Program walks on web site, clicks internal links, wait 20 seconds on each page
# and writes visited pages.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SeoWalker():

    def walk(self, url, amount):

        base_url = url
        self.driver = webdriver.Firefox()
        # driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(base_url)
        self.driver.implicitly_wait(10)
        a_links = self.driver.find_elements_by_xpath("//a[contains(@href,'"+url+"')] ")
        links_to_write = []

        for i in range (0, len(a_links)):

            if len(str(a_links[i].get_attribute("href"))) > len(base_url) + 1:

                if a_links[i].get_attribute("href") in links_to_write:
                    continue

                links_to_write.append(str(a_links[i].get_attribute("href")))

            if len(links_to_write) == amount:
                self.walk_inside(links_to_write)
                self.write_to_file(links_to_write)
                break

        print("The amount of links is " + str(len(links_to_write)))

    def walk_inside(self,links_array):
        driver = self.driver

        for link in links_array:
            driver.get(link)
            # здесь прокрутка страницы
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(30)
            print(link)

        driver.close()

    def write_to_file(self,links_array):
        # открыть файл и построчно добавлять новые линки после "прогулки"
        pass


sw = SeoWalker()
sw.walk("https://www.stranamam.ru/", 8)


