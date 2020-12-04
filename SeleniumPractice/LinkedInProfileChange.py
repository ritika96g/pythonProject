from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import autoit
from time import sleep
import os

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path='C:\\Users\\Ritikag\\PycharmProjects\\pythonProject\\Driver\\chromedriver.exe', options=options)
action = ActionChains(driver)

driver.get("https://www.linkedin.com/")

email_field = driver.find_element_by_xpath("//input[@autocomplete='username']")
driver.execute_script("arguments[0].value='ritika96g@gmail.com'", email_field)
password = driver.find_element_by_xpath("//input[@type='password']")
driver.execute_script("arguments[0].value='mobile@?123'", password)

sign_in = driver.find_element_by_xpath("//button[contains(text(),'Sign in')]")
driver.execute_script("arguments[0].click();", sign_in)

WebDriverWait(driver, 5).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
profile_icon = driver.find_element_by_xpath("//div[contains(@data-control-name,'profile_photo')]//img")
driver.execute_script("arguments[0].click();", profile_icon)

edit_profile_area_xpath = "//button[@aria-label='Profile photo']"
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, edit_profile_area_xpath)))
edit_profile_area = driver.find_element_by_xpath(edit_profile_area_xpath)
driver.execute_script("arguments[0].click();", edit_profile_area)
path = r"C:\Users\Ritikag\Downloads\Profile.jpeg"
# driver.execute_script("arguments[0].value= path", driver.find_element_by_xpath("//input[@id='image-selector__file-upload-input']"))
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class,'file-upload')]")))
driver.execute_script("document.getElementById('image-selector__file-upload-input').style.visibility='hidden'")
driver.find_element_by_id("image-selector__file-upload-input").send_keys(path)

# upload_photo = driver.find_element_by_xpath("//*[contains(@class,'file-upload')]")
# upload_photo.click()
# action.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
# action.send_keys(r"C:\Users\Ritikag\Downloads\Profile.jpeg").perform()

# without AutoIt
# autoit.win_wait_active("Open", 4)
# autoit.control_send("Open","Edit1", r"C:\Users\Ritikag\Downloads\Profile.jpeg")
# autoit.control_click("Open","Button1")
#
# time.sleep(3)

action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.ENTER).perform()



# autoit.win_wait_active("File Upload")
# autoit.send(r"C:\Users\Ritikag\Downloads\Profile.jpeg")
# autoit.send("{ENTER}")


# time.sleep(3)
# dialouge_box_id = driver.find_element_by_xpath("//div[@id='ember2145']")
# dialouge_text = driver.find_element_by_xpath("//body//div[contains(@class,'image-selector-modal')]//h2")
# print(dialouge_text.text)
# upload_photo_button = driver.find_element_by_xpath("//label[contains(text(),'Upload photo')]")
# driver.execute_script("arguments[0].click();", upload_photo_button)



