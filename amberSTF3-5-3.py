import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def by_selector():
    driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver.exe') 
    driver.get("https://antycaptcha.amberteam.pl:5443/stf/3-5-3?seed=000c0514-8b72-4558-9998-f68d954e84a7")
    h6 = driver.find_element(By.CSS_SELECTOR, "h6")
    h6.find_element(By.CSS_SELECTOR, "a").click()
    time.sleep(1)
    result = driver.find_elements(By.CSS_SELECTOR, "code")
    return result[1].text
    # driver.quit()

if __name__ == "__main__":
    print(by_selector())