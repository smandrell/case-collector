from cssselect import Selector
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import scrapy

SEARCH_TEXT = "%123%"

dfs = []

class CourtRecordScraper(scrapy.Spider):
    name = "record_scraper"

    start_urls = ['http://apps.marincounty.org/BeaconRoa/BeaconROASearch.aspx']

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        #initialize query array

        self.driver = webdriver.Chrome(executable_path="../resources/chromedriver-mac.exe", chrome_options=options)

    def parse(self, response):
        #parse for n different queries
        self.driver.get(url=response.url)
        case_num = self.driver.find_element_by_id("txtCaseNumber")
        case_num.send_keys(SEARCH_TEXT)
        search_button = self.driver.find_element_by_name("btnSearch")
        search_button.click()

        b_soup = BeautifulSoup(self.driver.page_source, "lxml")

        tables = b_soup.find_all('table')
        if not tables:
            return
        table = tables[0]
        df = pd.read_html(str(table))
        dfs.append(df)
        print(dfs)