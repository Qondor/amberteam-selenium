import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def button_and_text():
    driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver.exe') 
    driver.get("https://antycaptcha.amberteam.pl:5443/exercises/exercise2?seed=000c0514-8b72-4558-9998-f68d954e84a7")
    
    t14_text = driver.find_element(By.ID, "t14")
    t14_text.clear()
    t14_text.send_keys("Produce scene simply yeah.")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "btnButton1"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "solution"))).click()
    time.sleep(1)
    return driver.find_element(By.CSS_SELECTOR, ".wrap").text
    # driver.quit()

if __name__ == "__main__":
    print(button_and_text())