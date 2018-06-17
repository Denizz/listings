# Program walks on web site, clicks internal links, wait 20 seconds on each page
# and writes visited pages.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SeoWalker():
    def walk(self, url, amount):
        base_url = url
        driver = webdriver.Firefox()
        # driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        # с помощью цикла сделать поиск линков amount раз и сделать переход на них. Потом передать линк в write_to_file(link)
        a_links = driver.find_elements_by_xpath("//a[contains(@href,'"+url+"')] ")
        links_to_write = []
        for i in range (0, len(a_links)):
            if len(str(a_links[i].get_attribute("href"))) > len(base_url) + 3:
                links_to_write.append(str(a_links[i].get_attribute("href")))
                #print("link " + str(a_links[i].get_attribute("href")))

            if len(links_to_write) == 5:
                self.walk_inside(links_to_write)
                break
        print("The amount of links is " + str(len(links_to_write)))
        driver.close()

    def walk_inside(self,links_array):
        print(links_array)
        pass

    def write_to_file(self):
        # открыть файл и построчно добавлять новые линки после "прогулки"
        pass


sw = SeoWalker()
sw.walk("https://www.stranamam.ru", 5)

