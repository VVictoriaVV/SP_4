from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from SP_4.locators.locators_main_page import TestLocators


class PageOrderScooter:
 def __init__(self, driver):
    self.driver = driver

def check_button_order_on_down():
    driver.find_element(*button_order_on_down).click
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.page_order))

def check_button_order_on_up():
    driver.find_element(*button_order_on_up).click
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.page_order))

def set_name():
    driver.find_element(*field_name).send_keys("Виктория")


def set_surname():
    driver.find_element(*field_surname).send_keys("Герт")

def set_adress():
    driver.find_element(*field_adress).send_keys("Москва")
def set_station_tube():
    driver.find_element(*field_station_tube).send_keys("Бибирево")

def set_phone_number():
    driver.find_element(*field_phone_number).send_keys("89030555555")

def check_button_dalee():
    driver.find_elemnt(*button_dalee).click
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.page_order2))


def set_field_data():
    driver.find_element(*field_data).send_keys('02.12.2023')

def set_field_srok_arenda():
    driver.find_element(*field_srok_arenda).click()
    driver.find_element(*choose_srok).click()

def check_cvet_samokata():
    driver.find_element(*field_cvet_samokata).click()

def check_button_order_on_second_form_of_order():
    driver.find_element(*button_order_on_second_form_of_order).click
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.modal_window))

def check_modal_window():
    driver.find_element(*button_confirm_on_modal_window).click
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.success_modal_window))


def check_perehod_na_glavnuy():
    driver.get('https://qa-scooter.praktikum-services.ru/track?t=561301')
    driver.find_element(*logo).click
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.main_page))

def check_perehod_yandex():
    driver.get('https://qa-scooter.praktikum-services.ru/track?t=561301')
    driver.find_element(*logo_ya).click
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.new_page))





