import sys
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_by_alert():
    driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver.exe') 
    driver.get("https://antycaptcha.amberteam.pl:5443")
    driver.find_element(By.CSS_SELECTOR, ".row:nth-child(15) .u-full-width").click()
    driver.find_element(By.ID, "showAlert").click()
    alert = WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    text = alert.text
    alert.dismiss()
    driver.find_element(By.ID, "alertText").send_keys(text)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "solution"))).click()
    time.sleep(1)
    result = driver.find_elements(By.CSS_SELECTOR, "code")
    assert "OK. Good answer" in result[1].text
    driver.quit()