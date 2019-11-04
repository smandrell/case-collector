from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def run(search_text):
    SEARCH_TEXT = search_text

    url = 'http://apps.marincounty.org/BeaconRoa/BeaconROASearch.aspx'

    # Use the the correct chromedriver-*.exe for whatever OS your are using (mac, windows, linux)
    driver = webdriver.Chrome(executable_path='resources/chromedriver-mac.exe')

    driver.get(url=url)

    caseNumberElement = driver.find_element_by_id("txtCaseNumber")

    caseNumberElement.send_keys(SEARCH_TEXT)

    search_button = driver.find_element_by_name("btnSearch")

    search_button.click()

    soup = BeautifulSoup(driver.page_source, "lxml")

    table = soup.find_all('table')

    #print("HERE: " + str(table))
    #df = pd.read_html(str(table))
    #print(df)
    #print(df[0].iloc[:, 1])

    return len(table)

print(run("%13"))