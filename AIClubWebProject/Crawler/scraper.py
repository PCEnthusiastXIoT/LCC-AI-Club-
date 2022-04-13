import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# I'm defining this function a more or less hard coded extra arg, so I can work on web driving
def scrape_site(sample_url, extra_nav=""):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()

    driver.get(sample_url)

    time.sleep(5)
    # search_box = driver.find_element(By.NAME, "q")
    # search_button = driver.find_element(By.NAME, "btnK")

    # search_box.send_keys("Selenium")
    # search_button.click()

    # driver.find_element(By.NAME, "q").get_attribute("value")  # => "Selenium"
    if extra_nav == "get-started":
        get_started = driver.find_element(By.LINK_TEXT, "GET STARTED")
        get_started.click()

    src = driver.page_source
    # driver.quit()

    # time.sleep(5)

    # time.sleep(1)

    # driver.find_element(By.CSS_SELECTOR, '.main-cta.started').click()

    parser = BeautifulSoup(src, "html.parser")
    driver.close()
    return src
