import allure
from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.locators_main_page import TestLocators
from pages.base_page import BasePage


class PageOrderScooter(BasePage):
 def check_button_order_on_down():
    driver.find_element(*button_order_on_down).click
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.page_order))

def check_button_order_on_up():
    driver.find_element(*button_order_on_up).click
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.page_order))

def set_name(self,name):
    self.send_key(TestLocators.field_name,name)


def set_surname(self, last_name):
        self.send_key(TestLocators.field_surname, surname)

def set_adress(self,adress):
    self.send_key(TestLocators.field_adress,adress)

def set_station_tube(self,station_tube):
    self.find_element(TestLocators.field_station_tube,station_tube).click()
    self.send_key(TestLocators.field_station_tube,station_tube)
    self.send_key(TestLocators.field_station_tube, station_tube, Keys.ARROW_DOWN + Keys.ENTER)

def set_phone_number(self,phone_number):
    self.send_key(TestLocators.field_phone_number,phone_number)

def check_button_dalee(self):
    self.find_element(TestLocators.button_dalee).click()


def set_field_data(self, data):
    self.send_keys(TestLocators.field_data, data)

def set_field_srok_arenda(self, srok_arenda):
    self.find_elements(TestLocators.field_srok_arenda).click()
    self.find_elements(TestLocators.choose_srok).click()

def check_cvet_samokata(self, cvet_samokata):
    self.find_elements(TestLocators.field_cvet_samokata).click()

def check_button_order_on_second_form_of_order(self):
    self.find_element(TestLocators.button_order_on_second_form_of_order).click

def check_modal_window(self):
    text = self.find_element(TestLocators.button_confirm_on_modal_window).text
    return text

def check_perehod_na_glavnuy(self,driver):
    driver.get('https://qa-scooter.praktikum-services.ru/track?t=561301')
    self.find_element(TestLocators.logo).click


def check_perehod_yandex():
    driver.get('https://qa-scooter.praktikum-services.ru/track?t=561301')
    driver.find_element(*logo_ya).click







