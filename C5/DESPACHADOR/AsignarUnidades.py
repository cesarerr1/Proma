# from cProfile import label
# from tkinter import messagebox
# from nose.tools import assert_true
# import HtmlTestRunner
import time
import unittest
from datetime import datetime
from io import open
from htmlrunner import HTMLRunner

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import WebDriverWait


def archivo_log_tiempos(text):
    now = datetime.now()
    tiempo = now.strftime("%H:%M:%S")
    log = open("../../../../Downloads/log.txt", "a", encoding="utf-8")
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
        usuario.send_keys("QA05")
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
            archivo_log_tiempos("Cargo login")
        except (RuntimeError, TypeError, NameError):
            archivo_log_tiempos("No cargo login")

        # ERUM
        driver.find_element_by_id("3").click()

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

        # incrementa la iteracion
        for x in range(0, 1):
            # Cambia el controlador a la ventana o pestana original
            driver.switch_to.window(win_ser_local)
            time.sleep(3)
            # EVENTO
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                                'html[1]/body[1]/app-root[1]/app-home-despachador[1]/div[1]/div[1]/div[2]/app-eventos-grid[1]/div[1]/div[1]/div[1]/div[1]'))).click()
                archivo_log_tiempos("Cargo seleccion evento")
            except (RuntimeError, TypeError, NameError):
                archivo_log_tiempos("No seleccion evento")

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
            # EVENTO

            # CLICK EN CAMBIAR AMARILLO
            bandera = True
            valor = 1

            while bandera:
                data = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                       f"//div[contains(@class,'grid lista-unidades')]/div[{valor}]/div/div[1]/div[1]/app-recursos-icons/*[local-name() = 'svg']"))).get_attribute(
                    'style')
                if data.find("rgb(255, 255, 255);") >= 0:
                    bandera = False
                else:
                    bandera = True
                    valor = valor + 1

            # CLICK EN CAMBIAR AMARILLO
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                f"//div[contains(@class,'grid lista-unidades')]/div[{valor}]/div[1]/div[1]/div[3]/button[2]"))).click()
                archivo_log_tiempos("Cargo evento amarillo")
            except (RuntimeError, TypeError, NameError):
                archivo_log_tiempos("No cargo evento amarillo")

            # CLICK EN EL BOTON DE ACEPTAR
            driver.find_element_by_xpath("//span[text()='Aceptar']").click()
            time.sleep(20)
            # CLICK EN EL BOTON DE CAMBIAR A ROJO
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                f"//div[contains(@class,'grid lista-unidades')]/div[{valor}]/div[1]/div[1]/div[3]/button[2]"))).click()
                archivo_log_tiempos("Cargo evento rojo")
            except (RuntimeError, TypeError, NameError):
                archivo_log_tiempos("No cargo evento rojo")

            # CLICK EN ACEPTAR
            driver.find_element_by_xpath("//span[text()='Aceptar']").click()
            time.sleep(15)
            # CLICK EN CERRAR EVENTO
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                f"//div[contains(@class,'grid lista-unidades')]/div[{valor}]/div[1]/div[1]/div[3]/button[2]"))).click()
                archivo_log_tiempos("Cargo evento cerrado")
            except (RuntimeError, TypeError, NameError):
                archivo_log_tiempos("No cargo evento cerrado")

            # CLICK EN ACEPTAR
            driver.find_element_by_xpath("//span[text()='Aceptar']").click()
            time.sleep(15)

            for win_ser_1 in driver.window_handles:
                if win_ser_1 != win_ser_local:
                    driver.switch_to.window(win_ser_1)
                    break
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mat-form-field-infix'])[3]"))).click()
            time.sleep(5)
            msj = driver.find_element_by_id("mat-input-2")
            msj.send_keys("todo ok")
            time.sleep(1)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "mat-option-164"))).click()
            time.sleep(5)
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='col-12 contenedor-botones']//button[1]"))).click()
                archivo_log_tiempos("Fin del proceso")
            except (RuntimeError, TypeError, NameError):
                archivo_log_tiempos("No fin del proceso")
            time.sleep(9)

            for win_ser_1 in driver.window_handles:
                if win_ser_1 != win_ser_local:
                    driver.switch_to.window(win_ser_1)
                    break
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//input[@role='combobox'])[2]"))).click()
            time.sleep(3)
            msjs = driver.find_element_by_id("Descripcion general")
            msjs.send_keys("todo ok")
            time.sleep(1)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//span[text()='AFIRMATIVO SITUACIÓN JURÍDICA ACLARADA']"))).click()
            time.sleep(3)
            driver.find_element_by_xpath("//button[text()='Aceptar']").click()
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

    def createEvent(self):
        driver.find_element_by_id("mat-checkbox-1").click()
        driver.find_element_by_xpath("//button[@id='0']/span").click()

        wait.until(EC.number_of_windows_to_be(2))
        # Recorrelas hasta encontrar el controlador de la nueva ventana
        for win_ser_1 in driver.window_handles:
            if win_ser_1 != win_ser_local:
                driver.switch_to.window(win_ser_1)
                break
        driver.close()

        cont = 100
        i = 1
        # Cambia el controlador a la ventana o pestana original
        driver.switch_to.window(win_ser_local)
        time.sleep(3)
        # EVENTO

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
    # unittest.main(testRunner=HTMLRunner.HTMLRunner())
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
