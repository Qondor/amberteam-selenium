import sys
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_by_selector():
    driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver.exe') 
    driver.get("https://antycaptcha.amberteam.pl:5443")
    driver.find_element(By.CSS_SELECTOR, ".five:nth-child(4) > .u-full-width").click()
    test_tag = driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > em").text
    hX = driver.find_element(By.CSS_SELECTOR, f"{test_tag[1:3]}")
    hX.find_element(By.CSS_SELECTOR, "a").click()
    time.sleep(1)
    result = driver.find_elements(By.CSS_SELECTOR, "code")
    assert "OK. Good answer" in result[1].text
    driver.quit()