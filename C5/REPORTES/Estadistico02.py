import time
import unittest
from datetime import datetime
from io import open

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def archivo_log(fecha, folio, desc):
    # existearchivo = os.path.isfile("log.txt")
    log = open("../../../../Downloads/log.txt", "w", encoding="utf-8")
    log.write("Fecha de generación: " + time.strftime(
        "%d/%m/%y") + "\n" + "Hora de ejecución: " + fecha + "\n" + "Folio: " + folio.text + "\n" + "Descripción: " + "\n" + desc.text)
    log.write("\n-------------------------------------------------------\n")
    log.close()
    return True


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
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        host = "http://52.9.236.138:9596"
        # host = "http://qa-promad.opensystems.mx"
        driver.get(host)
        now = datetime.now()

        try:
            login = WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.ID, "mat-input-0")))
            archivo_log_tiempos("Cargo login")
        except (RuntimeError, TypeError, NameError):
            archivo_log_tiempos("No cargo login")

        driver.find_element_by_id("mat-input-0").send_keys("CFLORES")
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

        time.sleep(20)

        numeroS = 1
        i = 1
        while i <= numeroS:
            print("Clic para abrir calendario")
            # Folio desde
            driver.find_element_by_xpath("//input[contains(@placeholder,'Desde')]").send_keys("C5/20200916/30")
            time.sleep(5)
            # Folio hasta
            driver.find_element_by_xpath("//input[contains(@placeholder,'Hasta')]").send_keys("C5/20200916/30")
            time.sleep(5)

            print("Seleccionando Radio")
            Seleccionar = driver.find_element_by_xpath("//mat-radio-button[@id='mat-radio-10']/label/div/div")
            Seleccionar.click()
            time.sleep(3)
            print("Selecciono por la hora")
            driver.find_element_by_xpath("//i[contains(@class,'fa fa-file-pdf-o fz-24 icons')]").click()
            time.sleep(3)
            print("Exportando pdf")
            i += 1
            time.sleep(10)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
