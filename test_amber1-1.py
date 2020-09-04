import sys
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_button_clicker():
    driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver.exe') 
    driver.get("https://antycaptcha.amberteam.pl:5443")
    driver.find_element(By.CSS_SELECTOR, ".row:nth-child(4) > .four:nth-child(1) > .button").click()
    
    x = 2
    while x < 5:
        if driver.find_element(By.CSS_SELECTOR, f"tr:nth-child({x}) code").text == "B1":
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "btnButton1"))).click()
        else:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "btnButton2"))).click()
        time.sleep(1)
        x += 1

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "solution"))).click()
    time.sleep(1)
    assert "OK. Good answer" in driver.find_element(By.CSS_SELECTOR, ".wrap").text
    driver.quit()