import selenium.webdriver
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://apps.marincounty.org/BeaconRoa/BeaconROASearch.aspx'

driver = selenium.webdriver.Chrome(executable_path='chromedriver.exe')

driver.get(url=url)

soup = BeautifulSoup(driver.page_source, "lxml")

inputs = soup.find_all('input', type='text')

for input in inputs:
    print(input.get('id'))


#### IDEA ####
# Just take the search text and hit every possible input field
# Concat all data and return results


