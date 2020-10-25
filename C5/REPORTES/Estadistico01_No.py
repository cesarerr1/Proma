from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from datetime import datetime
from io import open
import unittest, time, re, codecs, os


def archivo_log(fecha, folio, desc):
    # existearchivo = os.path.isfile("log.txt")
    log = open("log.txt", "w", encoding="utf-8")
    log.write("Fecha de generación: " + time.strftime("%d/%m/%y") + "\n" + "Hora de ejecución: " + fecha + "\n" + "Folio: " + folio.text + "\n" + "Descripción: " + "\n" + desc.text)
    log.write("\n-------------------------------------------------------\n")
    log.close()
    return True

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
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        #host = "http://52.9.236.138:9596"
        host = "http://qa-promad.opensystems.mx"
        driver.get(host)
        now = datetime.now()

        try:
            login = WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.ID, "mat-input-0")))
            archivo_log_tiempos("Cargo login")
        except (RuntimeError, TypeError, NameError):
            archivo_log_tiempos("No cargo login")


        driver.find_element_by_id("mat-input-0").send_keys("QA09")
        time.sleep(1)
        driver.find_element_by_id("mat-input-1").send_keys("C5")
        time.sleep(1)
        driver.find_element_by_id("mat-input-2").send_keys("12345")
        time.sleep(1)
        driver.find_element_by_class_name("mat-raised-button").click()
        print("Termina login")

        #seleccionar perfil
        driver.find_element_by_class_name("icnIph").click()
        print("Perfil seleccionado")

        time.sleep(35)
        print("Clic para abrir calendario")
        #driver.find_element_by_xpath("//input[contains(@id,'376.46800757080456Desde')]").click()
        #driver.find_element_by_xpath("//div[text()='//*[@id='376.46800757080456Desde']']").click()
        #Folio desde
        driver.find_element_by_xpath("//input[contains(@placeholder,'Desde')]").send_keys("C5/20200916/30")
        time.sleep(1)
        #Folio hasta
        driver.find_element_by_xpath("//input[contains(@placeholder,'Hasta')]").send_keys("C5/20200916/30")
        time.sleep(3)
        #Agrupado por HORA
        #agrupadopor = driver.find_element_by_id("mat-radio-9-input")
        #agrupadopor = driver.find_element_by_xpath("/html/body/app-root/app-dashboard/div/div[2]/app-estadisticos/app-tiempo/app-filters-reports/div/div[3]/div[1]/div/app-radio-buttom/div/mat-radio-group/mat-radio-button[1]/label/div[1]/div[1]")
        #agrupadopor = driver.find_element_by_id("//label[@for='mat-radio-10-input']//div[@class='mat-radio-ripple mat-ripple']")
        # --- agrupadopor5 = driver.find_element_by_css_selector("label[for='mat-radio-9-input'] div[class='mat-radio-outer-circle']")

        # ---
        #agrupadopor = driver.find_element_by_xpath("//label[@for='mat-radio-9-input']//div[@class='mat-radio-inner-circle']")
        # driver.find_element_by_xpath("label[for='mat-radio-9-input'] div[class='mat-radio-inner-circle']")

        # -- 10
        #agrupadopor = driver.find_elements_by_css_selector("label[for='mat-radio-10-input'] div[class='mat-radio-outer-circle']").click()
        #agrupadopor = driver.find_element_by_xpath("//mat-radio-button[@id='mat-radio-9']/label[1]/div[1]/div[1]").click()
        print("Seleccionando Radio")
        driver.find_elements_by_xpath("//input[@id='mat-radio-9-input']").click()
        time.sleep(3)
        print("Selecciono por la hora")
        driver.find_element_by_xpath("//i[contains(@class,'fa fa-file-pdf-o fz-24 icons')]").click()
        time.sleep(3)
        print("Exportando pdf")


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
