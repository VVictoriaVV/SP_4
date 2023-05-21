class PageImportantQuestions:

 def __init__(self, driver):
    self.driver = driver

def check_button_skolko_stoit():
    driver.find_element(*button_skolko_stoit).click()
    but0 = driver.find_element(*but0)


def check_button_hochu_neskolko_samokatov():
    driver.find_element(*button_hochu_neskolko_samokatov).click()
    but1 = driver.find_element(*but1)


def check_button_kak_raschitivaetsya():
    driver.find_element(*button_kak_raschitivaetsya).click()
    but2 = driver.find_element(*but2)

def check_button_mozhno_li_zakazat():
    driver.find_element(*button_mozhno_li_zakazat).click()
    but3 = driver.find_element(*but3)


def check_button_mozhno_li_prodlit():
    driver.find_element(*button_mozhno_li_prodlit).click()
    but4 = driver.find_element(*but4)


def check_button_vi_privozite_zaryadku():
    driver.find_element(*button_vi_privozite_zaryadku).click()
    but5 = driver.find_element(*but5)

def check_button_mozhno_otmenit_zakaz():
    driver.find_element(*button_mozhno_otmenit_zakaz).click()
    but6 = driver.find_element(*but6)


def check_button_i_zhivu_za_mkadom():
    driver.find_element(* button_i_zhivu_za_mkadom).click()
    but7 = driver.find_element(*but7)
