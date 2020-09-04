import sys
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_seed_seeker():
    driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver.exe') 
    driver.get("https://antycaptcha.amberteam.pl:5443")
    driver.find_element(By.CSS_SELECTOR, ".row:nth-child(9) .u-full-width").click()
    seed = driver.find_element(By.CSS_SELECTOR, "code").text
    driver.get(f'https://antycaptcha.amberteam.pl/stf/3-2-1/solution?seed={seed[14:]}')
    result = driver.find_elements(By.CSS_SELECTOR, "code")
    assert "OK. Good answer" in result[1].text
    driver.quit()