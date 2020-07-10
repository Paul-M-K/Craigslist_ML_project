# this code was obtained by following https://github.com/vprusso/youtube_tutorials/blob/master/web_scraping_and_automation/selenium/craigstlist_scraper.py
# import libraries that will be needed for this code.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

import numpy as np

import pandas as pd


# construct a class.
class CraiglistScraper(object): # will hopefully make it esier to modify in the future
    def __init__(self, location, max_price): # define constructor
        self.location = location
        self.max_price = max_price

        #here we need to build the URL that we want to feed to the website
        self.url = f"http://{location}.craigslist.org/search/van/apa?van/apa?availabilityMode=0&bundleDuplicates=1&&min_price=300&max_price={max_price}&min_bathrooms=1&minSqft=100&availabilityMode=0&sale_date=all+dates"
        self.url_1 = f"http://{location}.craigslist.org/search/van/apa?van/apa?availabilityMode=0&bundleDuplicates=1&&min_price=300&max_price={max_price}&min_bathrooms=1&minSqft=100&availabilityMode=0&sale_date=all+dates&s=120"
        self.url_2 = f"http://{location}.craigslist.org/search/van/apa?van/apa?availabilityMode=0&bundleDuplicates=1&&min_price=300&max_price={max_price}&min_bathrooms=1&minSqft=100&availabilityMode=0&sale_date=all+dates&s=240"
        self.url_3 = f"http://{location}.craigslist.org/search/van/apa?van/apa?availabilityMode=0&bundleDuplicates=1&&min_price=300&max_price={max_price}&min_bathrooms=1&minSqft=100&availabilityMode=0&sale_date=all+dates&s=360"
        self.url_4 = f"http://{location}.craigslist.org/search/van/apa?van/apa?availabilityMode=0&bundleDuplicates=1&&min_price=300&max_price={max_price}&min_bathrooms=1&minSqft=100&availabilityMode=0&sale_date=all+dates&s=480"

        self.driver = webdriver.Firefox()                   # this will open up the web browser
        self.delay = 5                                      # delay to ensure that page will load 3s delay.
    def load_craigslist_url(self):
        self.driver.get(self.url)                           # calls the self.driver to get the self.url from the init
        try:                                                # ensure that page is loaded.
            wait = WebDriverWait(self.driver, self.delay)
            wait.until(EC.presence_of_all_elements_located((By.ID, "searchform")))
            print("Success: Page loaded")
        except TimeoutException:
            print("Error: Page did not load")

    # Now we want to intract the information on the page.
    @property
    def extract_post_information(self):
        title_list = []
        price_list = []
        lat_list = []
        long_list = []
        acc_list = []
        bed_list = []
        bath_list = []
        sqft_list = []
        id_list = []
        main_page = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(main_page, 'lxml')
        page_r = soup.findAll("span", {"class": "rangeTo"})
        totalcount = soup.findAll("span", {"class": "totalcount"})
        steps = int(int(totalcount[0].text)/int(page_r[0].text))
        page_range = int(page_r[0].text)
        for i in range(0, steps+1):
            if i == 0:
                for link in soup.findAll("a", {"class": "result-title hdrlnk"}):
                    house_page = urllib.request.urlopen(link["href"])
                    soup_new = BeautifulSoup(house_page,'lxml')
                    for link_price in soup_new.findAll("span", {"class": "price"}):
                        price_list.append(int(link_price.text.replace('$', '')))
                    for link_title in soup_new.findAll("span",{"id": "titletextonly"}):
                       title_list.append(link_title.text)
                    for link_loc in soup_new.findAll("div",{"id": "map"}):
                        lat_list.append(float(link_loc["data-latitude"]))
                        long_list.append(float(link_loc["data-longitude"]))
                        acc_list.append(int(link_loc["data-accuracy"]))
                    for link_loc in soup_new.findAll("span", {"class": "shared-line-bubble"}):
                        items = link_loc.text.split()
                        if len(items[0]) == 3:
                            bed_list.append(int(items[0].replace('BR','')))
                            bath_list.append(float(items[2].replace('Ba','')))
                        if len(items[0]) == 6:
                            sqft_list.append(int(items[0].replace('ft2','')))
            else:
                main_page = urllib.request.urlopen(self.url + "&s=" + str(page_range*i))
                soup = BeautifulSoup(main_page, 'lxml')
                for link in soup.findAll("a", {"class": "result-title hdrlnk"}):
                    house_page = urllib.request.urlopen(link["href"])
                    soup_new = BeautifulSoup(house_page,'lxml')
                    for link_price in soup_new.findAll("span", {"class": "price"}):
                        price_list.append(int(link_price.text.replace('$', '')))
                    for link_title in soup_new.findAll("span",{"id": "titletextonly"}):
                        title_list.append(link_title.text)
                    for link_loc in soup_new.findAll("div",{"id": "map"}):
                        lat_list.append(float(link_loc["data-latitude"]))
                        long_list.append(float(link_loc["data-longitude"]))
                        if link_loc["data-accuracy"] != 'number':
                            acc_list.append(int(link_loc["data-accuracy"]))
                    for link_loc in soup_new.findAll("span", {"class": "shared-line-bubble"}):
                        items = link_loc.text.split()
                        if len(items[0]) == 3:
                            bed_list.append(int(items[0].replace('BR','')))
                            bath_list.append(float(items[2].replace('Ba','')))
                        if len(items[0]) == 6:
                            sqft_list.append(int(items[0].replace('ft2','')))

        return title_list, price_list, lat_list, long_list, acc_list, bed_list, bath_list, sqft_list

    def quit(self):
        self.driver.close()

location = "vancouver"
max_price = "2000"

scraper = CraiglistScraper(location, max_price)
scraper.load_craigslist_url()
#scraper.extract_post_information()
title, price, lat, long, acc, bed, bath, sqft = scraper.extract_post_information
scraper.quit()

df = pd.DataFrame(list(zip(title, price, lat, long, acc, bed, bath, sqft)))
df.to_csv('craigslist_scraper.csv')