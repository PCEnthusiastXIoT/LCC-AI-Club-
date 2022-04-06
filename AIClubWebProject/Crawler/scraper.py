import time

from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.common.keys import Keys


def scrape_site(SAMPLE_URL):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("window-size=1920x1080")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)

    driver.get(SAMPLE_URL)

    time.sleep(5)

    for t in range(10):
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)

    for t in range(10):
        time.sleep(1)

        driver.find_element_by_css_selector('.additional_data').click()

    src = driver.page_source
    parer = BeautifulSoup(src, "html.parser")
    driver.close()
    return src, parser
