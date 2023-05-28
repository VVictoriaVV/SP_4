from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators_main_page import TestLocators
from pages.page_order_samokat import MainPage


class TestOrderScooter:
    @pytest.mark.parametrize('button_dalee, field_station_tube, field_name, field_surname, field_address, '
                             'field_phone_number',
                             [pytest.param(user_1.button_dalee, user_1.field_station_tube, user_1.field_name,user_1.field_surname, user_1.field_address,user_1.field_phone_number,user_1.index,user_1.color),
                              pytest.param(user_2.button_dalee, user_2.field_station_tube, user_2.field_name,user_2.field_surname, user_2.field_address,user_2.field_phone_number,user_2.index,user_2.color)])
    def test_order(self, driver, button_dalee, station_tube, name, surname,
                   adress, phone_number, date, index, color):
        main_page = MainPage(driver)
        order_page = OrderPageFillingData(driver)
        rent_page = RentPageFillingData(driver)
        main_page.accept_cookie()
        main_page.click_order(button_dalee)

        order_page.filling_order_data(
            field_name=name,
            field_surname=surname,
            field_adress=adress,
            field_station_tube=field_station_tube,
            phone_number=phone_number)

        order_page.click_next()

        rent_page.filling_about_rent_date(
            date=date,
            index=index,
            color=color_index)

        rent_page.click_on_button_to_order()
        rent_page.click_yes_on_modal_menu()

        assert "Заказ оформлен" in rent_page.completed_order(), 'Всплывающее окно с сообщением об успешном создании заказа должно отображаться.'

