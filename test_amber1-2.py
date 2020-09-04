import sys
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_button_and_text():
    driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver.exe') 
    driver.get("https://antycaptcha.amberteam.pl:5443")
    driver.find_element(By.CSS_SELECTOR, ".row:nth-child(4) > .four:nth-child(2) > .button").click()
    t14_text = driver.find_element(By.ID, "t14")
    t14_text.clear()
    t14_text.send_keys(driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) code:nth-child(1)").text)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "btnButton1"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "solution"))).click()
    time.sleep(1)
    assert "OK. Good answer" in driver.find_element(By.CSS_SELECTOR, ".wrap").text
    driver.quit()