import sys
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_radio_clicker():
    driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver.exe') 
    driver.get("https://antycaptcha.amberteam.pl:5443")
    driver.find_element(By.CSS_SELECTOR, ".row:nth-child(5) > .four:nth-child(1) > .button").click()
    radio = driver.find_element(By.CSS_SELECTOR, "td:nth-child(3) code").text
        
    driver.find_element_by_css_selector(f"input[type='radio'][value='v{radio[1]}0']").click()
    time.sleep(1)
    driver.find_element_by_css_selector(f"input[type='radio'][value='v{radio[4]}1']").click()
    time.sleep(1)
    driver.find_element_by_css_selector(f"input[type='radio'][value='v{radio[7]}2']").click()
    time.sleep(1)
    driver.find_element_by_css_selector(f"input[type='radio'][value='v{radio[10]}3']").click()
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "solution"))).click()
    time.sleep(1)
    assert "OK. Good answer" in driver.find_element(By.CSS_SELECTOR, ".wrap").text
    driver.quit()