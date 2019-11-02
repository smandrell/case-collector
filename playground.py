from bs4 import BeautifulSoup
import pandas as pd
import scrapy

SEARCH_TEXT = "%123"

dfs = []


def scrape_data(response):
    b_soup = BeautifulSoup(response.body, "lxml")
    tables = b_soup.find_all('table')
    if not tables:
        return
    table = tables[0]
    df = pd.read_html(str(table))
    dfs.append(df)


class CourtRecordScraper(scrapy.Spider):
    name = "court_records"

    start_urls = ['http://apps.marincounty.org/BeaconRoa/BeaconROASearch.aspx']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={"txtCaseNumber": SEARCH_TEXT},
            callback=scrape_data
        )
