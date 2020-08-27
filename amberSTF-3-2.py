from selenium import webdriver
from selenium.webdriver.common.by import By

def seed_seeker():
    driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver.exe') 
    driver.get("https://antycaptcha.amberteam.pl:5443/stf/3-2-1?seed=000c0514-8b72-4558-9998-f68d954e84a7")
    seed = driver.find_element(By.CSS_SELECTOR, "code").text
    driver.get(f'https://antycaptcha.amberteam.pl/stf/3-2-1/solution?seed={seed[14:]}')
    result = driver.find_elements(By.CSS_SELECTOR, "code")
    return result[1].text
    # driver.quit()

if __name__ == "__main__":
    print(seed_seeker())