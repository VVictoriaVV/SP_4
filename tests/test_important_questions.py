from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from SP_4.locators.locators_main_page import TestLocators


class TestImportantQuestionsPage():
    def __init__(self, driver):
        self.driver = driver

    def test_button_skolko_stoit(self):
        self.important_questions_page.check_button_skolko_stoit()
        expected_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        actual_text = self.driver.find_element(By.CSS_SELECTOR, ".some-element-class").text
        self.assertEqual(expected_text, actual_text)

    def test_button_hochu_neskolko_samokatov(self):
        self.important_questions_page.check_button_hochu_neskolko_samokatov()
        expected_text = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        actual_text = self.driver.find_element(By.CSS_SELECTOR, ".some-element-class").text
        self.assertEqual(expected_text, actual_text)

    def test_button_kak_raschitivaetsya(self):
        self.important_questions_page.check_button_kak_raschitivaetsya()
        expected_text = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        actual_text = self.driver.find_element(By.CSS_SELECTOR, ".some-element-class").text
        self.assertEqual(expected_text, actual_text)

    def test_button_mozhno_li_zakazat(self):
        self.important_questions_page.check_button_mozhno_li_zakazat()
        expected_text = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        actual_text = self.driver.find_element(By.CSS_SELECTOR, ".some-element-class").text
        self.assertEqual(expected_text, actual_text)

    def test_button_mozhno_li_prodlit(self):
        self.important_questions_page.check_button_mozhno_li_prodlit()
        expected_text = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        actual_text = self.driver.find_element(By.CSS_SELECTOR, ".some-element-class").text
        self.assertEqual(expected_text, actual_text)

    def test_button_vi_privozite_zaryadku(self):
        self.important_questions_page.check_button_vi_privozite_zaryadku()
        expected_text = "Самокат приезжает к вам с полной зарядкой."

    def test_check_button_mozhno_otmenit_zakaz(self):
        important_questions_page = ImportantQuestionsPage(self.driver)
        important_questions_page.check_button_mozhno_otmenit_zakaz()
        but6_text = important_questions_page.get_button_mozhno_otmenit_zakaz_text()
        assert but6_text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    def test_check_button_i_zhivu_za_mkadom(self):
        important_questions_page = ImportantQuestionsPage(self.driver)
        important_questions_page.check_button_i_zhivu_za_mkadom()
        but7_text = important_questions_page.get_button_i_zhivu_za_mkadom_text()
        assert but7_text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


