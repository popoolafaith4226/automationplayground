import time

from selenium import webdriver

from selenium.webdriver.common.by import By

#initializing thr browser
driver = webdriver.Chrome()

#launch the url
driver.get ("https://automationplayground.com/crm/login.html")

#expand the browser
driver.maximize_window()

#enter email

enter_email = driver.find_element (By.ID, "email-id")
enter_email.send_keys("faith@gmail.com")

enter_password = driver.find_element(By.ID, "password")
enter_password.send_keys("123345")

remember_me = driver.find_element(By.ID, "remember")
remember_me.click()

time.sleep(3)

submit_button = driver.find_element(By.ID, "submit-id")
submit_button.click()

time.sleep(3)

# click on new customer

new_customer = driver.find_element(By.ID, "new-customer")
new_customer.click()


# Add customer

add_email = driver.find_element (By.ID, "EmailAddress")
add_email.send_keys("james@gmail.com")

add_firstname = driver.find_element( By.ID, "FirstName")
add_firstname.send_keys("James")

last_name = driver.find_element(By.ID, "LastName")
last_name.send_keys("okoro")

add_city = driver.find_element(By.ID, "City")
add_city.send_keys("Lagos")

add_state = driver.find_element(By.ID, "StateOrRegion")
add_state.click()

click_state = driver.find_element(By.XPATH, "//*[@id='StateOrRegion']/option[14]")
click_state.click()

gender = driver.find_element(By.XPATH, "//*[@id='loginform']/div/div/div/div/form/div[6]/input[1]")
gender.click()

# add to promotional list

promotional_list = driver.find_element (By.XPATH, "//*[@id='loginform']/div/div/div/div/form/div[7]/input")
promotional_list.click()


# submit Button

submit_button = driver.find_element(By.XPATH, "//*[@id='loginform']/div/div/div/div/form/button")
submit_button.click()

time.sleep (3)

driver.close()

