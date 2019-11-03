from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

SEARCH_TEXT = "testtt"

url = 'http://apps.marincounty.org/BeaconRoa/BeaconROASearch.aspx'

driver = webdriver.Chrome(executable_path='resources/chromedriver-windows.exe')

driver.get(url=url)

caseNumberElement = driver.find_element_by_id("txtCaseType")

caseNumberElement.send_keys(SEARCH_TEXT)

search_button = driver.find_element_by_name("btnSearch")

search_button.click()

soup = BeautifulSoup(driver.page_source, "lxml")

table = soup.find_all('table')

print("HERE: " + str(table))

df = pd.read_html(str(table))

print(df)
#
# print("PAGE TITLE: " + driver.title)