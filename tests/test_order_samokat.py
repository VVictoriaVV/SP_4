from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from SP_4.locators.locators_main_page import TestLocators


class TestOrderScooter:
    def __init__(self, driver):
        self.driver = driver

    def test_button_order_on_down(self):
        driver.find_element(*button_order_on_down).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.page_order))
        page_order_text = driver.find_element(*TestLocators.page_order).text
        assert page_order_text == 'Для кого самокат'

    def test_button_order_on_up(self):
        driver.find_element(*button_order_on_up).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.page_order))
        page_order_text = driver.find_element(*TestLocators.page_order).text
        assert page_order_text == 'Для кого самокат'

    def test_fill_order_form(self):
        driver.find_element(*field_name).send_keys("Виктория")
        driver.find_element(*field_surname).send_keys("Герт")
        driver.find_element(*field_adress).send_keys("Москва")
        driver.find_element(*field_station_tube).send_keys("Бибирево")
        driver.find_element(*field_phone_number).send_keys("89030555555")
        driver.find_element(*button_dalee).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.page_order2))


        driver.find_element(*field_data).send_keys('02.12.2023')
        driver.find_element(*field_srok_arenda).click()
        driver.find_element(*choose_srok).click()
        driver.find_element(*field_cvet_samokata).click()
        driver.find_element(*button_order_on_second_form_of_order).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.modal_window))
        driver.find_element(*button_confirm_on_modal_window).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.success_modal_window))
        success_modal_window_text = driver.find_element(*TestLocators.success_modal_window).text
        assert success_modal_window_text == 'Заказ оформлен'

    def test_perehod_na_glavnuy(self):
        driver.get('https://qa-scooter.praktikum-services.ru/track?t=561301')
        driver.find_element(*logo).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.main_page))
        main_page_text = driver.find_element(*TestLocators.main_page).text
        assert main_page_text == 'Самокат'

    def test_perehod_yandex(self):
        driver.get('https://qa-scooter.praktikum-services.ru/track?t=561301')
        driver.find_element(*logo_ya).click()
        new_page_url = driver.current_url
        assert new_page_url == 'https://dzen.ru/?yredirect=true'