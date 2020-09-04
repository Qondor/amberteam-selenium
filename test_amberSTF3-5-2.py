import sys
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_by_class():
    driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver.exe') 
    driver.get("https://antycaptcha.amberteam.pl:5443")
    driver.find_element(By.CSS_SELECTOR, ".five:nth-child(3) > .u-full-width").click()
    test_class = driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > em").text
    driver.find_element(By.CLASS_NAME, f"{test_class}").click()
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "solution"))).click()
    time.sleep(1)
    assert "OK. Good answer" in driver.find_element(By.CLASS_NAME, "wrap").text
    driver.quit()