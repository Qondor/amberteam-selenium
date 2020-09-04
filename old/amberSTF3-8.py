import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def by_alert():
    driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver.exe') 
    driver.get("https://antycaptcha.amberteam.pl:5443/stf/3-8-1?seed=000c0514-8b72-4558-9998-f68d954e84a7")
    driver.find_element(By.ID, "showAlert").click()
    alert = WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    text = alert.text
    alert.dismiss()
    driver.find_element(By.ID, "alertText").send_keys(text)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "solution"))).click()
    time.sleep(1)
    result = driver.find_elements(By.CSS_SELECTOR, "code")
    return result[1].text
    # driver.quit()

if __name__ == "__main__":
    print(by_alert())