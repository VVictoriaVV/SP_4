import allure
from pages.page_order_samokat import MainPage

class TestCheckLogo:

    def test_click_on_logo_scooter(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/order")
        main_page = MainPage(driver)
        main_page.click_on_logo_scooter()
        main_page.checking_tabs()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"


    def test_click_on_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_logo_yandex()
        main_page.checking_tabs()
        assert driver.current_url == "https://dzen.ru/?yredirect=true"