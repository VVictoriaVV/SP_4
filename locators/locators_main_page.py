from selenium.webdriver.common.by import By

class TestLocators():

 title_questions_about_important = [By.XPATH, ".//div[text()='Вопросы о важном']"]  # Заголовок Вопросы о важном
menu = [By.XPATH, ".//*[@class='accordion']"]  # Гармошка с вопросами и ответами
questions_menu = [By.XPATH, ".//*[contains(@id, 'accordion__heading-')]"]  # Список вопросов
answers_menu = [By.XPATH, ".//*[contains(@id, 'accordion__panel-')]/p"]  # Список ответов
accept_cookies = [By.XPATH, ".//button[@class='App_CookieButton__3cvqF' and text()='да все привыкли']"]
button_order_on_down = [By.XPATH, ".//*[contains(@class, 'Button_Middle__1CSJM')]"]
button_order_on_up = [By.XPATH, ".//*[@class='Button_Button__ra12g']"]
page_order = [By.XPATH,'Order_Header__BZXOb']
field_name = [By.XPATH, ".//*[@placeholder='* Имя']"]
field_surname = [By.XPATH, ".//*[@placeholder='* Фамилия']"]
field_phone_number = [By.XPATH, ".//*[@placeholder='* Телефон: на него позвонит курьер']"]
field_station_tube = [By.XPATH, ".//*[@placeholder='* Станция метро']"]
field_adress = [By.XPATH, ".//*[@placeholder='* Адрес: куда привезти заказ']"]
button_dalee = [By.XPATH, ".//*[text()='Далее']"]
page_order2 = [By.XPATH,'Order_Header__BZXOb']
field_data = [By.XPATH, ".//*[@placeholder='* Когда привезти самокат']"]
field_srok_arenda = [By.XPATH, ".//*[@class='Dropdown-arrow']"]
choose_srok = [By.XPATH,'Dropdown-option is-selected']
dropdown_option = [By.XPATH,'Dropdown-option']
field_cvet_samokata = [By.XPATH,'Checkbox_Label__3wxSf']
button_order_on_second_form_of_order =  [By.XPATH, ".//*[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') " "and text()='Заказать']"]
modal_window = [By.XPATH,'Order_ModalHeader__3FDaJ']
button_confirm_on_modal_window = [By.XPATH,'Button_Button__ra12g Button_Middle__1CSJM']
success_modal_window = [By.XPATH, ".//*[@class='Order_ModalHeader__3FDaJ']"]
logo = [By.XPATH, ".//*[@alt='Scooter']"]
main_page = [By.XPATH,'Home_Header__iJKdX']
logo_ya = [By.XPATH, ".//*[@alt='Yandex']"]
new_page = [By.XPATH, ".//iframe[@class='dzen-search-arrow-common__frame' and @aria-label='Поиск Яндекса']"]