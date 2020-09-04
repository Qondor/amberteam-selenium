import sys
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_selecter():
    driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver.exe') 
    driver.get("https://antycaptcha.amberteam.pl:5443")
    driver.find_element(By.CSS_SELECTOR, ".row:nth-child(4) > .four:nth-child(3) > .button").click()
    select = Select(driver.find_element_by_id('s13'))
    value = driver.find_element(By.CSS_SELECTOR, "td:nth-child(3) > code").text
    select.select_by_value(value[4:])
    time.sleep(1)
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "solution"))).click()
    time.sleep(1)
    assert "OK. Good answer" in driver.find_element(By.CSS_SELECTOR, ".wrap").text
    driver.quit()