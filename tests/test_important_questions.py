import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators_main_page import TestLocators
from pages.page_important_questions import MainPage



class TestImportantQuestionsPage():

    def test_check_questions_and_descriptions(self):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        main_page.accept_cookie()
        base_page.scroll_down()
        main_page.check_answers_in_questions_about_important(question_index)
        actual_result = base_page.find_elements(MainPageLocators.answers_menu)[question_index].text
        expected_result = DataExample.dictionary_question_and_answers[base_page.find_elements(MainPageLocators.questions_menu)[question_index].text]
        assert actual_result == expected_result, 'Ответ на вопрос не совпадает со значением в словаре'


