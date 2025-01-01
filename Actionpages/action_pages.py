import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Loginlocators.locator import Login_locators, Add_new_customer, Enter_customer_details
from config.Config import Config


class login_pages:

    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)


    def enter_email(self, email):
        input_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_locators.EMAIL))
        input_email.send_keys(email)


    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_locators.PASSWORD))
        enter_password.send_keys(password)


    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_locators.LOGINBUTTON))
        login_button.click()


    def click_remember_me(self):
        click_remember = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_locators.REMEMBERME))
        click_remember.click()


class add_new_customer:

    def __init__(self, driver):
        self.driver = driver

    def add_a_new_customer(self):
        click_add_new_customer = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Add_new_customer.new_customer))
        click_add_new_customer.click()

class new_customer_email:

    def __init__(self, driver):
        self.driver = driver

    def input_new_customer_email(self, user_email):
        fix_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Enter_customer_details.new_customer_email))
        fix_email.send_keys(user_email)

class new_customer_Firstname:

    def __init__(self, driver):
        self.driver = driver

    def input_new_customer_firstname(self, user_firstname):
        fix_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Enter_customer_details.new_customer_first_name))
        fix_firstname.send_keys(user_firstname)


class new_customer_lastname:
    def __init__(self, driver):
        self.driver = driver

    def input_new_customer_lastname(self,user_lastname):
        fix_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Enter_customer_details.new_customer_last_name))
        fix_lastname.send_keys(user_lastname)

class new_customer_city:
    def __init__(self, driver):
        self.driver = driver

    def input_new_customer_lastname(self,user_city):
        fix_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Enter_customer_details.new_customer_city))
        fix_city.send_keys(user_city)

class click_state:
    def __init__(self, driver):
        self.driver = driver

    def click_customer_state(self):
        fix_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Enter_customer_details.new_customer_state))
        fix_state.click()

class select_state:
    def __init__(self, driver):
        self.driver = driver

    def select_user_state(self):
        fix_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Enter_customer_details.select_state))
        fix_state.click()

        time.sleep(3)

class select_gender:
    def __init__(self, driver):
        self.driver = driver

    def select_user_gender(self):
        pick_gender= WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Enter_customer_details.gender))
        pick_gender.click()







