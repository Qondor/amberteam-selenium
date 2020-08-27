import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def by_class():
    driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver.exe') 
    driver.get("https://antycaptcha.amberteam.pl:5443/stf/3-5-2?seed=000c0514-8b72-4558-9998-f68d954e84a7")
    driver.find_element(By.CLASS_NAME, "then").click()
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "solution"))).click()
    time.sleep(1)
    return driver.find_element(By.CLASS_NAME, "wrap").text
    # driver.quit()

if __name__ == "__main__":
    print(by_class())