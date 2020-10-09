# from cProfile import label
# from tkinter import messagebox

# from nose.tools import assert_true
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
        driver.get("http://demos-promad.opensystems.mx:9191")
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
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"icnAtencionTactica"))).click()
            archivo_log_tiempos("Cargo login")
        except (RuntimeError, TypeError, NameError):
            archivo_log_tiempos("No cargo login")

        driver.find_element_by_id("mat-checkbox-1").click()
        time.sleep(1)
        # ingresar
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//button[@id='0']/span"))).click()
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
        time.sleep(30)

        i = 1
        while i <= 50:
            # EVENTO
            print("dar clic para el evento nuevo")
            time.sleep(1)
            archivo_log_tiempos("Nuevo incidente")
            driver.find_element_by_xpath("//body/app-my-app[1]/app-home-despachador[1]/div[1]/div[1]/div[2]/app-eventos-grid[1]/div[1]/app-toolbar-eventos-grid[1]/mat-toolbar[1]/button[15]/span[1]/*[1]").click()
            time.sleep(1)
            #wait.until(EC.number_of_windows_to_be(1))
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(1)
            #driver.find_element_by_id("mat-input-13").send_keys("algo")
            driver.find_element_by_xpath("//textarea[@id='mat-input-13']").send_keys("algo")
            time.sleep(1)
            driver.find_element_by_xpath("//mat-icon[contains(text(),'public')]").click()
            print("Abriendo buscador")
            time.sleep(40)

            # Ingresando al iframe de la barra de herramientas
            driver.switch_to.frame(driver.find_element_by_xpath("//body/app-my-app[1]/app-sub-map[1]/div[1]/div[1]/iframe[1]"))
            time.sleep(2)
            print("dentro del iframe")
            driver.find_element_by_id("sidepanelsearchsigacontrol").click()
            time.sleep(2)
            # alcaldia =

            # colonia
            driver.find_element_by_id("cmbColonia_I").send_keys("LA CRUZ")
            print("Buscando la colonia")
            time.sleep(2)
            driver.find_element_by_id("cmbColonia_L").click()
            time.sleep(2)
            archivo_log_tiempos("Seleciono la colonia")

            # buscar
            driver.find_element_by_xpath("//html/body/form/div[3]/div[4]/div/div/div[9]/div/a").click()
            time.sleep(2)

            # Primera opcion
            ubicacion = driver.find_element_by_xpath("//*[@id='BootstrapGridBusquedaPuntual_DXDataRow0']/td[2]/a").click()
            driver.switch_to.default_content()
            time.sleep(2)
            # driver.close()
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(2)
            driver.find_element_by_xpath("//span[contains(text(),'ACEPTAR')]").click()
            print("aceptar")
            time.sleep(2)
            #Origen
            driver.find_element_by_xpath("//body/app-my-app[1]/app-llamada-ronda[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[2]/app-select-search[1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[2]").click()
            time.sleep(2)
            #Tipo Origen
            driver.find_element_by_xpath("//span[contains(text(),'ALERTA VECINAL')]").click()
            time.sleep(2)
            # Motivo
            driver.find_element_by_xpath("//body/app-my-app[1]/app-llamada-ronda[1]/div[1]/form[1]/div[2]/div[2]/div[1]/div[2]/app-select-search[1]/mat-form-field[1]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[2]/div[1]").click()
            time.sleep(2)
            # Tipo Motivo
            driver.find_element_by_xpath("//span[contains(text(),'ACCIDENTE-CHOQUE CON PRENSADOS')]").click()
            time.sleep(2)
            #Aceptar
            driver.find_element_by_xpath("//body/app-my-app[1]/app-llamada-ronda[1]/div[1]/form[1]/div[2]/div[2]/div[2]/div[3]/button[1]").click()
            time.sleep(7)

            # Obtiene folio
            obtienefolio = driver.find_element_by_xpath("//html/body/app-my-app/app-llamada-ronda/div/form/div/div/div[2]/span")
            if obtienefolio is not None:
                print("Se genero el folio")
            print(obtienefolio.text)

            #Toma imagen
            fecha2 = time.strftime("%H:%M:%S")
            date_stamp = fecha2.replace(" ", "_").replace(":", "_").replace("-", "_")
            file_name = date_stamp + ".png"
            self.driver.save_screenshot(file_name)
            archivo_log_tiempos("Genero el evento")
            time.sleep(2)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(7)
            archivo_log_tiempos("Termino por completo")
            i += 1

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
