from pages.base_page import BasePage

class PageImportantQuestions(BasePage):

 def __init__(self, driver):
    self.driver = driver

def check_button_skolko_stoit(self):
    self.driver.find_element(*button_skolko_stoit).click()
    self.but0 = driver.find_element(*but0)


def check_button_hochu_neskolko_samokatov(self):
    self.driver.find_element(*button_hochu_neskolko_samokatov).click()
    self.but1 = driver.find_element(*but1)


def check_button_kak_raschitivaetsya(self):
    self.driver.find_element(*button_kak_raschitivaetsya).click()
    self.but2 = driver.find_element(*but2)

def check_button_mozhno_li_zakazat(self):
    self.driver.find_element(*button_mozhno_li_zakazat).click()
    self.but3 = driver.find_element(*but3)


def check_button_mozhno_li_prodlit(self):
    self.driver.find_element(*button_mozhno_li_prodlit).click()
    self.but4 = driver.find_element(*but4)


def check_button_vi_privozite_zaryadku(self):
    self.driver.find_element(*button_vi_privozite_zaryadku).click()
    self.but5 = driver.find_element(*but5)

def check_button_mozhno_otmenit_zakaz(self):
    self.driver.find_element(*button_mozhno_otmenit_zakaz).click()
    but6 = driver.find_element(*but6)


def check_button_i_zhivu_za_mkadom(self):
    self.driver.find_element(* button_i_zhivu_za_mkadom).click()
    self.but7 = driver.find_element(*but7)
