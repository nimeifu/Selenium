import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def login(user_email, pwd):
    """
    Login to the site
    :param user_email: (str) user's email
    :param pwd: (str) user's password
    :return:
    """
    email = driver.find_element(By.XPATH, '//*[@id="email"]')
    email.send_keys(str(user_email))
    time.sleep(2)
    passwd = driver.find_element(By.XPATH, '//*[@id="password"]')
    passwd.send_keys(str(pwd))
    time.sleep(2)
    sign_in = driver.find_element(By.XPATH, '//*[@id="submit_button"]')
    sign_in.click()
    time.sleep(2)


def search_title(job_name):
    job_title = WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, '//*['
                                                                                                           '@id'
                                                                                                           '="search1"]')))
    job_title.clear()
    job_title.send_keys(str(job_name))
    time.sleep(2)


def search_location():
    job_location = WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, '//*['
                                                                                                              '@id'
                                                                                                              '="location1"]')))
    job_location.clear()
    job_location.send_keys("Remote Nationwide")
    time.sleep(2)
    press_search = driver.find_element(By.XPATH,
                                       '//*[@id="main"]/div/div[3]/div[1]/div/div/section[1]/form/div[5]/input')
    time.sleep(2)
    press_search.click()
    time.sleep(1)


def nums_of_jobs(job_nums):
    load_more_jobs = driver.find_element(By.XPATH, '//*[@id="primary"]/section[2]/div/button')
    load_more_jobs.click()
    whole_page = driver.find_element(By.TAG_NAME, 'html')
    count = 0
    while count < job_nums:
        whole_page.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        count = len(driver.find_elements(By.XPATH, one_click_apply))


def apply_for_job():
    apply_button = driver.find_element(By.XPATH, one_click_apply)
    apply_button.click()
    time.sleep(2)


if __name__ == '__main__':
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.ziprecruiter.com/authn/login")
    one_click_apply = '//*[contains(text(),"1-Click Apply")]'

    login()  # enter user account here
    search_title() # enter a job you are looking for
    search_location()

    nums_of_jobs(100)

    while True:
        try:
            apply_for_job()
        except:
            break

    # html=driver.find_element(By.TAG_NAME,'html')
    # while True:
    #     html.send_keys(Keys.PAGE_DOWN)
    #     time.sleep(2)

    # SCROLL_PAUSE_TIME = 2
    #
    # # Get scroll height
    # last_height = driver.execute_script("return document.body.scrollHeight")
    #
    # while True:
    #     # Scroll down to bottom
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    #     # Wait to load page
    #     time.sleep(SCROLL_PAUSE_TIME)
    #
    #     # Calculate new scroll height and compare with last scroll height
    #     new_height = driver.execute_script("return document.body.scrollHeight")
    #     if new_height == last_height:
    #         break
    #     last_height = new_height

    # driver.get("https://www.ziprecruiter.com/authn/login")
    # time.sleep(0.2)
