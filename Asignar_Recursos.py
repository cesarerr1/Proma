from cProfile import label
from tkinter import messagebox

from nose.tools import assert_true
from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
#import HtmlTestRunner
from tkinter import *
import unittest, time, re



class UntitledTestCase(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
        self.driver.set_window_size(1400, 1000)
        self.driver.implicitly_wait(30)
        #self.base_url = "http://promad.opensystems.mx:8081/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_cerrar_evento (self):
        driver = self.driver
        driver.get("http://qa-promad.opensystems.mx/")
        wait = WebDriverWait(driver, 15)
        # Almacena el ID de la ventana original
        win_ser_local = driver.current_window_handle
        # Comprueba que no existen otras ventanas abiertas previamente
        assert len(driver.window_handles) == 1
        time.sleep(1)

        #USUARIO
        usuario = driver.find_element_by_id("mat-input-0")
        usuario.send_keys("QA05")
        usuario.send_keys(Keys.ENTER)
        time.sleep(1)

        #CENTRO
        centro = driver.find_element_by_id("mat-input-1")
        centro.send_keys("C5")
        centro.send_keys(Keys.ENTER)
        time.sleep(1)

        #PASSWORD
        clave = driver.find_element_by_id("mat-input-2")
        clave.send_keys("12345")
        clave.send_keys(Keys.ENTER)
        time.sleep(1)

    #MENU
        driver.find_element_by_id("icnAtencionTactica").click()
        time.sleep(1)
    #ANPR
        #driver.find_element_by_id("8").click()

    #BOMBEROS
        #driver.find_element_by_id("1").click()

    #CRUZ ROJA
        #driver.find_element_by_id("2").click()

    #ERUM
        driver.find_element_by_id("3").click()

    #FGJ
        #driver.find_element_by_id("7").click()

    #GAS NAT
        #driver.find_element_by_id("4").click()

    #LINEA DE MANDO
        #driver.find_element_by_id("15").click()

    #MB
        #driver.find_element_by_id("5").click()

    #RTP
        #driver.find_element_by_id("9").click()

    #SACMEX
        #driver.find_element_by_id("10").click()

    #SEDEMA
        #driver.find_element_by_id("12").click()

    #SEPROBAN
        #driver.find_element_by_id("19").click()

    #SERVICIOS PERICIALES
        #driver.find_element_by_id("20").click()

    #SGIRPC
        #driver.find_element_by_id("13").click()

    #SOBSE
        #driver.find_element_by_id("6").click()

    #SSC
        #driver.find_element_by_id("14").click()

    #SSC TRANSITO
        #driver.find_element_by_id("18").click()
        
    #STCM
        #driver.find_element_by_id("16").click()

    #TE
        #driver.find_element_by_id("17").click()


        time.sleep(1)
        driver.find_element_by_id("mat-checkbox-1").click()
        time.sleep(1)
        #ingresar
        driver.find_element_by_xpath("//button[@id='0']/span").click()
        time.sleep(1)

        # Espera a la nueva ventana o pestaña
        wait.until(EC.number_of_windows_to_be(2))
        # Recorrelas hasta encontrar el controlador de la nueva ventana
        for win_ser_1 in driver.window_handles:
            if win_ser_1 != win_ser_local:
                driver.switch_to.window(win_ser_1)
                break
        driver.close()

        cont = 100
        i=1
        # Cambia el controlador a la ventana o pestaña original
        driver.switch_to.window(win_ser_local)
        time.sleep(3)
        # EVENTO


        numero = int(raw_input("\nIngresa el numero de EVENTOS a cerrar: "))
        #numero = messagebox.Dialog(int(raw_input("\nIngresa el numero de EVENTOS a cerrar: ")))


        #numero = label(miFrame, text="eventos")


        while i <= numero:
            #evento = driver.find_element_by_xpath("//mat-card/h4")
            #assert_true(len(evento) == True)

            driver.find_element_by_xpath("//mat-card/h4").click()
            time.sleep(2)
            # Espera a la nueva ventana o pestaña
            wait.until(EC.number_of_windows_to_be(2))
            # Recorrelas hasta encontrar el controlador de la nueva ventana
            for win_ser_1 in driver.window_handles:
                if win_ser_1 != win_ser_local:
                    driver.switch_to.window(win_ser_1)
                    break
            driver.close()
            time.sleep(2)
            driver.switch_to.window(win_ser_local)
            time.sleep(3)
           
            time.sleep(3)

            driver.switch_to.window(win_ser_local)
            time.sleep(5)
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
