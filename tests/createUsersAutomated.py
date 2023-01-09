
import time as t
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import traceback

#################################################


def launchBrowser(username, password, email, fname, lname, options, webD):

    driver = webdriver.Chrome(webD, options=options)
    driver.get("http://127.0.0.1:8000/register/")

    search_input = driver.find_element(By.XPATH, '//*[@id="id_username"]')
    search_input.send_keys(username)

    search_input = driver.find_element(By.XPATH, '//*[@id="id_password1"]')
    search_input.send_keys(password)

    search_input = driver.find_element(By.XPATH, '//*[@id="id_password2"]')
    search_input.send_keys(password)

    search_input = driver.find_element(By.XPATH, '//*[@id="id_email"]')
    search_input.send_keys(email)

    search_input = driver.find_element(By.XPATH, '//*[@id="id_first_name"]')
    search_input.send_keys(fname)

    search_input = driver.find_element(By.XPATH, '//*[@id="id_last_name"]')
    search_input.send_keys(lname)

    search_btn = driver.find_element(By.XPATH, '/html/body/div/form/a/button')
    driver.execute_script('arguments[0].click();', search_btn)
    t.sleep(0.2)
    #################################################
    # Part with creating profile
    #################################################
    # not used atm
    driver.quit()


#################################################
options = Options()
# options.headless = True
webD = ChromeDriverManager().install()
driver = webdriver.Chrome(webD, options=options)
driver.get("http://127.0.0.1:8000/register/")
driver.quit()
#################################################

#################################################
username = 'AutoTestUserZ0'
password = 'DNovtta9TezM6S'
email_damain = '@mail.com'
fname = 'tomek'
lname = 'paluch'
#################################################

start_time = t.time()


try:
    for x in range(2):
        launchBrowser(username + str(x), password, username +
                      str(x) + email_damain, fname, lname, options, webD)

    print("sequential took ", (t.time() - start_time), " seconds")
except Exception:
    print("Exception occurred:")
    traceback.print_exc()
