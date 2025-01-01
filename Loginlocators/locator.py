from selenium.webdriver.common.by import By


class Login_locators:
    EMAIL = (By.ID, "email-id")
    PASSWORD = (By.ID, "password")
    LOGINBUTTON = (By.ID, "submit-id")
    REMEMBERME = (By.ID,"remember")

class Add_new_customer:
    new_customer = (By.ID,"new-customer")

class Enter_customer_details:
    new_customer_email = (By.XPATH, "//*[@id='EmailAddress']")
    new_customer_first_name = (By.XPATH, "//*[@id='FirstName']")
    new_customer_last_name = (By.XPATH, "//*[@id='LastName']")
    new_customer_city = (By.XPATH, "//*[@id='City']")
    new_customer_state = (By.XPATH, "//*[@id='StateOrRegion']")
    select_state = (By.XPATH, "//*[@id='StateOrRegion']/option[16]")
    gender = (By.XPATH, "//*[@id='loginform']/div/div/div/div/form/div[6]/input[1]")











