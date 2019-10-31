from selenium import webdriver
from bs4 import BeautifulSoup
from threading import Thread
import pandas as pd

## wildcard characters = Marin -> %, Santa Clara -> *

SEARCH_TEXT = "%123"

url = 'http://apps.marincounty.org/BeaconRoa/BeaconROASearch.aspx'

options = webdriver.ChromeOptions()
options.add_argument(argument="headless")  # This opens the browser silently in the background

driver = webdriver.Chrome(executable_path='resources/chromedriver.exe', options=options)

driver.get(url=url)

soup = BeautifulSoup(driver.page_source, "lxml")

inputs = soup.find_all('input', type='text')

driver.quit()


def handle_field(browser, input_field):

    element = browser.find_element_by_id(input_field)
    element.send_keys(SEARCH_TEXT)
    search_button = browser.find_element_by_name("btnSearch")
    search_button.click()

    b_soup = BeautifulSoup(browser.page_source, "lxml")
    tables = b_soup.find_all('table')
    if not tables:
        return
    table = tables[0]
    df = pd.read_html(str(table))
    dfs.append(df)

    browser.quit()


dfs = []
threads = []

for field in inputs:
    options = webdriver.ChromeOptions()
    options.add_argument(argument="headless")  # This opens the browser silently in the background
    driver = webdriver.Chrome(executable_path='resources/chromedriver.exe', options=options)
    driver.get(url=url)

    field_name = field.get('id')
    process = Thread(target=handle_field, args=[driver, field_name])
    process.start()
    threads.append(process)

for t in threads:
    t.join()

print(len(dfs))

#### IDEA ####
# Just take the search text and hit every possible input field
# Concat all data and return results
