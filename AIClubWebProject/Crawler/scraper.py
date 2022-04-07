import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def scrape_site(sample_url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    driver.get(sample_url)

    time.sleep(5)

    #time.sleep(1)

    #driver.find_element(By.CSS_SELECTOR, '.main-cta.started').click()

    src = driver.page_source
    parser = BeautifulSoup(src, "html.parser")
    driver.close()
    return src, parser
