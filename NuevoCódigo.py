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
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://promad.opensystems.mx:8081/")
        time.sleep(1)
        driver.find_element_by_id("mat-input-0").send_keys("CROJAS")
        time.sleep(1)
        driver.find_element_by_id("mat-input-1").send_keys("C5")
        time.sleep(1)
        driver.find_element_by_id("mat-input-2").send_keys("12345")
        time.sleep(1)
        driver.find_element_by_class_name("mat-raised-button").click()
        time.sleep(1)
        driver.find_element_by_class_name("icnAtencion").click()
        time.sleep(4)
        driver.find_element_by_id("mat-input-3").send_keys("5525194378")
        time.sleep(3)
        driver.find_element_by_id("mat-input-3").send_keys(Keys.CONTROL + Keys.ENTER)
        time.sleep(4)

        # Ingresando al iframe de la barra de herramientas
        driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='siga']"))
        time.sleep(1)
        print("dentro del iframe")
        driver.find_element_by_id("sidepanelsearchsigacontrol").click()
        time.sleep(3)
        colonia = driver.find_element_by_id("cmbColonia_I")
        colonia.send_keys("joya")
        print("Buscando la colonia")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/form/div[3]/div[3]/div/div[1]/div[9]/div[1]/a").click()
        time.sleep(2)
        # Tercer respuesta
        ubicacion = driver.find_element_by_xpath(
            "/html[1]/body[1]/form[1]/div[5]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[4]/td[2]/a[1]").click()
        driver.switch_to.default_content()

        time.sleep(3)
        evencercano = driver.find_element_by_xpath("//span[contains(text(),'Aceptar')]")
        print(evencercano.is_displayed())


        # if evencercano == "True":
        driver.find_element_by_xpath("//mat-icon[contains(text(),'close')]").click()

        # -- Datos incidente
        time.sleep(2)
        driver.find_element_by_id("mat-input-13").send_keys("DESCRIPCION UNO")
        time.sleep(1)
        driver.find_element_by_id("mat-input-13").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_xpath("//mat-select[@id='mat-select-4']/div/div/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("//span[contains(text(),'ABANDONO-ANIMAL')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//span[contains(text(),'ENVIAR A DESPACHO')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[contains(text(),'GUARDAR')]").click()

        time.sleep(7)
        print("termino completo")


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
