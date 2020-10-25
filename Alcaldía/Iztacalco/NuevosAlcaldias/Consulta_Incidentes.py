#from cProfile import label
#from tkinter import messagebox
#from nose.tools import assert_true

from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import unittest, time, re, codecs, os
from datetime import datetime
from io import open
from selenium.common.exceptions import TimeoutException


def archivo_log_tiempos(text):
    now = datetime.now()
    tiempo = now.strftime("%H:%M:%S")
    #log = open("../../../../Downloads/log.txt", "a", encoding="utf-8")
    log = open("log.txt", "a", encoding="utf-8")
    log.write("\n" + tiempo + " - " + text)
    log.close()
    print(tiempo + "-" + text)
    return True


class UntitledTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\dchrome\chromedriver.exe")
        self.driver.set_window_size(1400, 1000)
        self.driver.implicitly_wait(30)
        # self.base_url = "http://promad.opensystems.mx:8081/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_cerrar_evento(self):
        driver = self.driver
        driver.get("http://qa-promad.opensystems.mx/")
        wait = WebDriverWait(driver, 15)
        # Almacena el ID de la ventana original
        win_ser_local = driver.current_window_handle
        # Comprueba que no existen otras ventanas abiertas previamente
        assert len(driver.window_handles) == 1
        time.sleep(1)

        # USUARIO
        usuario = driver.find_element_by_id("mat-input-0")
        usuario.send_keys("CFLORES")
        usuario.send_keys(Keys.ENTER)
        time.sleep(1)

        # CENTRO
        centro = driver.find_element_by_id("mat-input-1")
        centro.send_keys("C5")
        centro.send_keys(Keys.ENTER)
        time.sleep(1)

        # PASSWORD
        clave = driver.find_element_by_id("mat-input-2")
        clave.send_keys("12345")
        clave.send_keys(Keys.ENTER)
        time.sleep(1)

        # MENU
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "icnAtencionTactica"))).click()
            archivo_log_tiempos("Cargo Login")
        except (RuntimeError, TypeError, NameError):
            archivo_log_tiempos("No cargo login")

        # SOBSE
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='SOBSE (SECRETARÍA DE OBRA']"))).click()

        time.sleep(1)
        driver.find_element_by_id("mat-checkbox-1").click()
        time.sleep(1)
        # ingresar
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@id='0']/span"))).click()
            archivo_log_tiempos("Cargo ingreso")
        except (RuntimeError, TypeError, NameError):
            archivo_log_tiempos("No cargo ingreso")

        # Espera a la nueva ventana o pestana
        wait.until(EC.number_of_windows_to_be(2))
        # Recorrelas hasta encontrar el controlador de la nueva ventana
        for win_ser_1 in driver.window_handles:
            if win_ser_1 != win_ser_local:
                driver.switch_to.window(win_ser_1)
                break
        driver.close()

        # Cambia el controlador a la ventana o pestana original
        driver.switch_to.window(win_ser_local)
        time.sleep(3)
        # MENU
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//button[contains(@class,'d-flex align-items-center')]//i[1]"))).click()
            archivo_log_tiempos("Cargo Menu")
        except (RuntimeError, TypeError, NameError):
            archivo_log_tiempos("No cargo Menu")

        # CONSULTA DE INCIDENTES
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//div[@class='menu-left-item ng-star-inserted']/following-sibling::div"))).click()
            archivo_log_tiempos("Cargo Consulta de Incidentes")
        except (RuntimeError, TypeError, NameError):
            archivo_log_tiempos("No cargo Consulta de Incidentes")

        for win_ser_1 in driver.window_handles:
            if win_ser_1 != win_ser_local:
                driver.switch_to.window(win_ser_1)
                break
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='Institución']"))).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='mat-option-text']//div)[3]"))).click()
        # CLICK EN BUSCAR
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class,'d-flex justify-content-end')]//span[1]"))).click()
            archivo_log_tiempos("Cargo Datos de Incidentes")
        except (RuntimeError, TypeError, NameError):
            archivo_log_tiempos("No cargo Datos de Incidentes")
        time.sleep(10)

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
