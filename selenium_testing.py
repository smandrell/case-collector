import selenium.webdriver
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://apps.marincounty.org/BeaconRoa/BeaconROASearch.aspx'

driver = selenium.webdriver.Chrome(executable_path='chromedriver.exe')

driver.get(url=url)

caseNumberElement = driver.find_element_by_id("txtCaseNumber")

caseNumberElement.send_keys('%123')

search_button = driver.find_element_by_name("btnSearch")

search_button.click()

soup = BeautifulSoup(driver.page_source, "lxml")

# inputs = soup.find_all('input')
# print("INPUTS: " + str(inputs))

table = soup.find_all('table')[0]

df = pd.read_html(str(table))

print(df)

print("PAGE TITLE: " + driver.title)
