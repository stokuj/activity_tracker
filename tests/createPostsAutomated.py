
import time as t
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#################################################
def launchBrowser(username, password, options,webD):

    driver = webdriver.Chrome(webD,options=options)
    driver.get("http://127.0.0.1:8000/login/")
    
    search_input =  driver.find_element(By.XPATH, '//*[@id="id_username"]')
    search_input.send_keys(username)

    search_input =  driver.find_element(By.XPATH, '//*[@id="id_password"]')
    search_input.send_keys(password)
    
    search_btn  =  driver.find_element(By.XPATH, '/html/body/div/form/a/button')
    driver.execute_script('arguments[0].click();', search_btn)
    t.sleep(2)
    #################################################
    ### We are logged in
    
    search_btn =  driver.find_element(By.XPATH, '/html/body/nav/div/div[1]/ul/li[2]/a')
    driver.execute_script('arguments[0].click();', search_btn)
    
    search_input =  driver.find_element(By.XPATH, '//*[@id="id_text"]')
    search_input.send_keys('Automated post test')

    search_btn =  driver.find_element(By.XPATH, '/html/body/div/form/button')
    driver.execute_script('arguments[0].click();', search_btn)
    
    driver.quit() 
#################################################   
options = Options()
options.headless = True
webD =  ChromeDriverManager().install()
driver =webdriver.Chrome(webD,options=options)
driver.get("http://127.0.0.1:8000/login/")
driver.quit()   
#################################################
  
#################################################
username        = 'AutoTestUserX0'
password        = 'DNovtta9TezM6S'
email_damain    = '@mail.com'
fname           = 'tomek'
lname           = 'paluch'
#################################################

start_time = t.time()

for x in range(1, 9):     
    launchBrowser(username + str(x), password,options,webD)
    
print("sequential took ", (t.time() - start_time), " seconds")   
