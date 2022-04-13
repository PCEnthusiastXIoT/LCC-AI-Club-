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
    # driver = webdriver.Chrome()

    # driver.get("https://www.google.com")
    driver.get(sample_url)
    # driver.title  # => "Google"

    # driver.implicitly_wait(0.5)
    time.sleep(5)
    # search_box = driver.find_element(By.NAME, "q")
    # search_button = driver.find_element(By.NAME, "btnK")

    # search_box.send_keys("Selenium")
    # search_button.click()

    # driver.find_element(By.NAME, "q").get_attribute("value")  # => "Selenium"

    src = driver.page_source
    # driver.quit()


    # time.sleep(5)

    # time.sleep(1)

    # driver.find_element(By.CSS_SELECTOR, '.main-cta.started').click()

    parser = BeautifulSoup(src, "html.parser")
    driver.close()
    return src
