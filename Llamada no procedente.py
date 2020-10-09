from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC

import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
        self.driver.set_window_size(1400, 1000)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://34.226.133.73:9191/login")
        time.sleep(1)
        driver.find_element_by_id("mat-input-0").send_keys("YOSORIO")
        time.sleep(1)
        driver.find_element_by_id("mat-input-1").send_keys("C5")
        time.sleep(1)
        driver.find_element_by_id("mat-input-2").send_keys("12345")
        time.sleep(1)
        driver.find_element_by_class_name("mat-raised-button").click()
        time.sleep(1)
        driver.find_element_by_class_name("icnAtencion").click()
        time.sleep(4)
        driver.find_element_by_id("mat-input-3").send_keys("5511130396")
        time.sleep(3)
        driver.find_element_by_id("mat-input-3").send_keys(Keys.CONTROL + Keys.ENTER)
        time.sleep(4)

        #Botón de llamada no procedente
        driver.find_element_by_xpath("//span/img").click()
        time.sleep(4)

        # abrir nueva pagina
        driver.execute_script("window.open('');")
        time.sleep(2)

        driver.switch_to.window(driver.window_handles[1])
        driver.get("http://34.226.133.73:9191/operador-dialogos/llamada-no-procedente/registrar/eyJudW1lcm9UZWwiOiI1NTExMTMwMzk2IiwiaWRPcmlnZW4iOjEsInByZWZvbGlvIjoiUEM1LzIwMjAwNzE1LzIzNDU4IiwibHVnYXIiOm51bGx9")
        time.sleep(2)

        #Seleccionar opción llamada de broma
        driver.find_element_by_xpath("//tr[4]/td").click()
        time.sleep(2)

        #Seleccionar botón aceptar
        driver.find_element_by_xpath("//div[3]/div/button").click()
        time.sleep(2)

        def is_element_present(self, how, what):
            try:
                self.driver.find_element(by=how, value=what)
            except NoSuchElementException as e:
                return False
            return True

        def is_alert_present(self):
            try:
                self.driver.switch_to_alert()
            except NoAlertPresentException as e:
                return False
            return True

        def close_alert_and_get_its_text(self):
            try:
                alert = self.driver.switch_to_alert()
                alert_text = alert.text
                if self.accept_next_alert:
                    alert.accept()
                else:
                    alert.dismiss()
                return alert_text
            finally:
                self.accept_next_alert = True

        def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)

    if __name__ == "__main__":
        unittest.main()





