from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

selenium = webdriver.Chrome()
selenium.implicitly_wait(10)
selenium.get("http://127.0.0.1:8080/polls/")
print("polls page")
# selenium.find_element(By.PARTIAL_LINK_TEXT,"What's up?").click()
selenium.find_element(By.ID,1).click()
print(selenium.current_url)
selenium.find_element(By.XPATH,"//input[@type='radio' and @value='1']").click()
selenium.find_element(By.XPATH,"//input[@type='radio' and @value='1']").click()
sleep(10)
selenium.quit()
