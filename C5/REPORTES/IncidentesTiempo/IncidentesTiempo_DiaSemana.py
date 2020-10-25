from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from htmlrunner import HTMLRunner
from datetime import datetime
import unittest, time, re, codecs, os


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\dchrome\chromedriver.exe")
        self.driver.set_window_size(1400, 1000)
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        # host = "http://52.9.236.138:9596"
        host = "http://qa-promad.opensystems.mx"
        driver.get(host)
        now = datetime.now()

        driver.find_element_by_id("mat-input-0").send_keys("QA04")
        time.sleep(1)
        driver.find_element_by_id("mat-input-1").send_keys("C5")
        time.sleep(1)
        driver.find_element_by_id("mat-input-2").send_keys("12345")
        time.sleep(1)
        driver.find_element_by_class_name("mat-raised-button").click()
        print("Termina login")

        # seleccionar perfil
        driver.find_element_by_class_name("icnIph").click()
        print("Perfil seleccionado")
        time.sleep(40)
        print("Clic para abrir calendario")

        i = 1
        while i <= 1:
            time.sleep(2)
            # Folio desde
            # driver.refresh()
            driver.find_element_by_xpath("//input[contains(@placeholder,'Desde')]").send_keys("C5/20200710/1")
            time.sleep(2)
            # Folio hasta
            driver.find_element_by_xpath("//input[contains(@placeholder,'Hasta')]").send_keys("C5/20201010/1")
            time.sleep(2)

            print("Seleccionando Radio")
            driver.find_element_by_xpath("//mat-radio-button[@id='mat-radio-10']/label/div/div").click()
            time.sleep(3)
            print("Importa en PDF")
            driver.find_element_by_xpath("//i[contains(@class,'fa fa-file-pdf-o fz-24 icons')]").click()
            time.sleep(3)
            print("Importa en Excel")
            driver.find_element_by_xpath("//i[contains(@class,'fa fa-file-excel-o fz-24 icons')]").click()
            time.sleep(10)
            print("limpiando formulario")
            driver.find_element_by_xpath("//i[contains(@class,'fa fa-eraser fz-22 icons')]").click()
            i += 1

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HTMLRunner.HTMLRunner(output='Crea resultado'))
    # unittest.main()
