from cssselect import Selector
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import scrapy

SEARCH_TEXT = "%123"

dfs = []


class CourtRecordScraper(scrapy.Spider):
    name = "record_scraper"

    start_urls = ['http://apps.marincounty.org/BeaconRoa/BeaconROASearch.aspx']

    # def __init__(self):
    #     self.driver = webdriver.Chrome(executable_path='../resources/chromedriver-windows.exe')

    def parse(self, response):
        # self.driver.get(url=response.url)
        # caseNum = self.driver.find_element_by_id("txtCaseNumber")
        # caseNum.send_keys(SEARCH_TEXT)
        # search_button = self.driver.find_element_by_name("btnSearch")
        # search_button.click()
        #
        # b_soup = BeautifulSoup(self.driver.page_source, "lxml")
        #
        # tables = b_soup.find_all('table')
        # if not tables:
        #     return
        # table = tables[0]
        # df = pd.read_html(str(table))
        # dfs.append(df)
        # print(dfs)

        # self.scrape_data(self.driver.page_source)

        return scrapy.FormRequest.from_response(
            response,
            formid="form1",
            formdata={"txtCaseNumber": SEARCH_TEXT,
                      '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first(),
                      '__EVENTVALIDATION': response.css('input#__EVENTVALIDATION::attr(value)').extract_first()},
            callback=self.scrape_data
        )

    def scrape_data(self, response):
        b_soup = BeautifulSoup(response.body, "lxml")
        tables = b_soup.find_all('table')
        if not tables:
            return
        table = tables[0]
        df = pd.read_html(str(table))
        dfs.append(df)
        print("HEREE")
        print(dfs)
