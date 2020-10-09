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
        time.sleep(1)
        alcaldia = driver.find_element_by_id("cmbMunicipio_I").click()
        time.sleep(1)
        alcaldia = driver.find_element_by_id("cmbMunicipio_L_LBI0LBL").click()
        time.sleep(3)

        colonia = driver.find_element_by_id("cmbColonia_I").send_keys("SAN MARTIN XOCHINAHUAC")
        print("Buscando la colonia")
        time.sleep(1)
        colonia1 = driver.find_element_by_id("cmbColonia_L").click()
        time.sleep(1)

        buscar = driver.find_element_by_xpath("//*[@id='default-tab-1']/div[9]/div[1]").click()
        time.sleep(1)

        # Primera opcion
        ubicacion = driver.find_element_by_xpath("//*[@id='BootstrapGridBusquedaPuntual_DXDataRow0']/td[2]/a").click()
        driver.switch_to.default_content()
        time.sleep(3)

        catalogoclave = driver.find_element_by_xpath(
            "/html/body/app-my-app/app-home-operador/div/div[2]/div[3]/app-crear-evento/div/form/div[2]/div[1]/mat-form-field/div/div[1]/div[3]").click()
        time.sleep(3)

        # Abandono animal
        driver.find_element_by_xpath("//*[@id='mat-option-23']/span").click()
        time.sleep(1)

        # -- Datos incidente
        time.sleep(2)
        driver.find_element_by_id("mat-input-13").send_keys("DESCRIPCION 123PROBANDO")
        time.sleep(1)
        driver.find_element_by_id("mat-input-13").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_xpath("//span[contains(text(),'ENVIAR A DESPACHO')]").click()
        time.sleep(2)

        # objeto involucrada boton
        driver.find_element_by_xpath(
            "/html/body/app-my-app/app-home-operador/div/div[2]/div[3]/app-crear-evento/div/form/div[4]/div[2]/div/div/button[4]/span").click()
        time.sleep(3)
        # abrir nueva pagina
        driver.execute_script("window.open('');")

        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.get(
            "http://promad.opensystems.mx:8081/common/datos-complementarios/objetos/involucrados/form/ABANDONO-ARTEFACTO%20EXPLOSIVO/C5*20200706*1577/69/null")
        time.sleep(1)
        driver.find_element_by_id("mat-input-0").send_keys("12")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='mat-select-0']/div/div[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='mat-option-2']/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='mat-select-1']/div/div[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='mat-option-13']/span").click()
        time.sleep(1)
        driver.find_element_by_id("mat-input-1").send_keys("120")
        time.sleep(1)
        driver.find_element_by_id("mat-input-2").send_keys("Ejercicio de practica")
        time.sleep(1)
        driver.find_element_by_xpath(
            "/html/body/app-my-app/app-armas-involucradas/div/app-armas-involucradas-form/form/div[3]/div/button[2]").click()
        time.sleep(1)

        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)

        driver.find_element_by_xpath(
            "/html/body/app-my-app/app-home-operador/div/div[2]/div[3]/app-crear-evento/div/div[2]/button/span/span").click()
        time.sleep(1)

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
