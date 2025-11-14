from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.cnarios.com/challenges/login-flow")

driver.find_element(By.XPATH,"//input[@id='«r1»']").send_keys("admin")
driver.find_element(By.XPATH,"//input[@id='«r2»']").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,"button[class*='MuiButton-contained']").click()
webdriver_wait = WebDriverWait(driver, 10)
webdriver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div strong")))
print(driver.find_element(By.CSS_SELECTOR, "div strong").text)