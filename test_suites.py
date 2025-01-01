import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Actionpages.action_pages import login_pages, add_new_customer, new_customer_email, new_customer_Firstname, \
    new_customer_lastname, new_customer_city, click_state, select_state, select_gender
from config.Config import Config

@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode

    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()



@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = login_pages(driver)
    login_page.login_url(Config.BASEURL)
    return login_page

def test_automation_lab_login_page(login):
    login.enter_email(Config.EMAIL)
    login.enter_password(Config.PASSWORD)
    login.click_remember_me()
    login.click_login_button()


def test_add_new_customer(login):
    adding_new_customer = add_new_customer(login.driver)
    adding_new_customer.add_a_new_customer()

def test_new_customer_email(login):
    input_new_customer_email = new_customer_email(login.driver)
    input_new_customer_email.input_new_customer_email(Config.NEWEMAIL)

def test_new_customer_firstname(login):
    input_new_customer_firstname = new_customer_Firstname(login.driver)
    input_new_customer_firstname.input_new_customer_firstname(Config.NEWUCUSTOMER_FIRSTNAME)

def test_new_customer_lastname(login):
    input_new_customer_lastname = new_customer_lastname(login.driver)
    input_new_customer_lastname.input_new_customer_lastname(Config.NEWUCUSTOMER_LASTNAME)

def test_new_customer_city(login):
    input_new_customer_city = new_customer_city(login.driver)
    input_new_customer_city.input_new_customer_lastname(Config.CITY)

def test_state(login):
    click_customer_state = click_state(login.driver)
    click_customer_state.click_customer_state()

def test_select_state(login):
    select_customer_state = select_state(login.driver)
    select_customer_state.select_user_state()

def test_gender(login):
    select_new_user_gender = select_gender(login.driver)
    select_new_user_gender.select_user_gender()