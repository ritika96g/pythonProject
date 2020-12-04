from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(executable_path='C:\\Users\\Ritikag\\PycharmProjects\\pythonProject\\Driver\\chromedriver.exe')
action = ActionChains(driver)
driver.get("https://www.amazon.in/s?k=one+plus&ref=nb_sb_noss_2")
time.sleep(3)
driver.maximize_window()

product_details_dictionary = {}

Product_Name_list = driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2")
rating_under_list = driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2//following::div[2]/span")
rating_under_list_star_rating = driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2//following::div[2]/span[1]")
rating_under_list_rating_count = driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2//following::div[2]/span[2]")
price_under_list = driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2//following::div[3]")
price_value_under_list = driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2//following::div[3]//span[@class='a-price']")


for index in range(len(Product_Name_list)):
    driver.execute_script("arguments[0].scrollIntoView(true);", Product_Name_list[index])
    print("Product Name : ", Product_Name_list[index].text)
    # print("Rating of product : ", rating_under_list[index].get_attribute("aria-label"), rating_under_list[index].text)
    print("Star Rating of product : ", rating_under_list_star_rating[index].get_attribute("aria-label"), " Global Rating Counts : ", rating_under_list_rating_count[index].text)
    print("Price of Product : ", price_under_list[index].text)
    print("Price Value : " , price_value_under_list[index].text)


# For tab clicking
# for e in range(len(Product_Name_list)-1):
#     if e == 0:
#        driver.execute_script("arguments[0].scrollIntoView(false);", Product_Name_list[e])
#        Product_Name_list[e].click()
#        window_ofProduct = driver.window_handles[e]
#        if window_ofProduct != main_window:
#             driver.switch_to.window(window_ofProduct)
#             time.sleep(3)
#             child_window = driver.window_handles[e]
#             time.sleep(3)
#             driver.close()
#     else:
#         break
            # print("Product Name : ", driver.title)
            # time.sleep(5)
            # if window_ofProduct != onePlus_Window:
            #     product_name = driver.find_element_by_xpath("//span[@id='productTitle']").text
            #     print(product_name)
            #     product_price = driver.find_element_by_xpath("//span[@id='mbc-price-1']").text
            #     print(product_price)
            # driver.switch_to.window(onePlus_Window)
