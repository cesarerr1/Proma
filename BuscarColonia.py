# -*- coding: utf-8 -*-
from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get(
            "http://sigacloudqa.digitalbyte.mx/SIGA.aspx?token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHRlbnNpb24iOiJFWFQxIiwic2Vzc2lvblNvY2tldEFudGVyaW9yIjoiMjE4NSIsInJvbGVzVXN1YXJpbyI6W3siaWRSb2wiOiIyIiwiaWRSb2xVc3VhcmlvIjoiMjEzIiwibm9tYnJlUm9sIjoiUk9MX09QRVJBRE9SIiwiZGVzY3JpcGNpb24iOiJPcGVyYWRvciJ9LHsiaWRSb2wiOiIzIiwiaWRSb2xVc3VhcmlvIjoiMjI4Iiwibm9tYnJlUm9sIjoiUk9MX0RFU1BBQ0hPIiwiZGVzY3JpcGNpb24iOiJEZXNwYWNobyJ9LHsiaWRSb2wiOiI1IiwiaWRSb2xVc3VhcmlvIjoiMjQzIiwibm9tYnJlUm9sIjoiUk9MX1NVUEVSVklTT1IiLCJkZXNjcmlwY2lvbiI6IlN1cGVydmlzb3IgdGVsZWZvbmlzdGEifSx7ImlkUm9sIjoiNiIsImlkUm9sVXN1YXJpbyI6IjI1OCIsIm5vbWJyZVJvbCI6IlJPTF9BRE1JTklTVFJBRE9SIiwiZGVzY3JpcGNpb24iOiJBZG1pbmlzdHJhZG9yIn0seyJpZFJvbCI6IjgiLCJpZFJvbFVzdWFyaW8iOiIyNzMiLCJub21icmVSb2wiOiJST0xfUkVQT1JURVMiLCJkZXNjcmlwY2lvbiI6IlJlcG9ydGVzIn1dLCJ1c2VyX25hbWUiOiJZT1NPUklPIiwibm9tYnJlVXN1YXJpbyI6IllPU09SSU8gWU9TT1JJTyIsInV1aWQiOiI1IiwiYXV0aG9yaXRpZXMiOlsiUk9MX09QRVJBRE9SIiwiUk9MX1JFUE9SVEVTIiwiUk9MX0RFU1BBQ0hPIiwiUk9MX1NVUEVSVklTT1IiLCJST0xfQURNSU5JU1RSQURPUiJdLCJjbGllbnRfaWQiOiJhbmd1bGFyYXBwIiwicGFyYW1ldHJvU2lzdGVtYSI6eyJjbGF2ZSI6IlRJRU1QT19MTEFNQURBX09QRSIsImRlc2NyaXBjaW9uIjoiVElFTVBPIFFVRSBUQVJEQVJBIFVOQSBMTEFNQURBIEFMIE9QRVJBRE9SOiBFTCBWQUxPUiBTT04gTE9TIFNFR1VORE9TIiwidmFsb3IiOiIxMCJ9LCJkYXRvc0VxdWlwbyI6eyJpZEVxdWlwbyI6MSwiaWRFeHRlbnNpb25UZWxlZm9uaWNhIjoxLCJub21icmVFeHRlbnNpb24iOiJFWFQxIn0sInNlc3Npb25Tb2NrZXQiOiIyMTk2IiwiZXh0Q2FyYnluZSI6IjAiLCJpZF91c3VhcmlvIjoiNDE2Iiwic2NvcGUiOlsicmVhZCIsIndyaXRlIl0sImV4cCI6MTU5Njc3NzcxNiwianRpIjoiMjRlM2Q0YWEtZjUxYy00ZDU2LWFjODQtZTI1MDVhNjE1YTlhIn0.K8UGBgjQ7fyVt43VrRldyzFPxNqeg9V6QzEcE4uEky1ROMcWKyHJu42h1Xk5v3Xh5LOpv-bZY94YG98rPm7G96LTAc4kLcdIh9GkB9oceK-IdtiwTIFE5dgMHEGtCAyJztmhBk8VQ1w5fQU4z9AGWcuEt41Xnz78UBFgunVwoEPjLhsbJlLmuSoQJJ6QcLtUHaiKu8ar6YpKXCEFqOnv3x0Tkl9gv_koHQj5H_-9bjfPvV71cwmmH-v5rRKKsLwZqjEH892RqBPwhGl-IU18MT-erNfN80omD0Q33xQO1O5rISPaaNHQMkQvHvkOpynAi8hrZYGpk4N4719UXxE_bQ&role=ROL_DESPACHO&hostname=DESKTOP-HVFRH99")
        #driver.get("http://sigacloud2.mapstrategic.mx/alertacloud/siga.html")
        time.sleep(1)
        #driver.switch_to.frame(driver.find_element_by_id("siga"))
        time.sleep(1)
        print("-- Dentro del iframe")
        driver.find_element_by_id("sidepanelsearchsigacontrol").click()
        time.sleep(2)

    #Ciclio
        i = 1
        numero = int(raw_input("\nIngresa el numero de EVENTOS a crear: "))
        while i <= numero:


        # alcaldia =
            print("-- Intruduciendo alcaldia")
            driver.find_element_by_id("cmbMunicipio_I").clear()
            time.sleep(1)
            driver.find_element_by_id("cmbMunicipio_I").send_keys("Benito Juarez")
            time.sleep(1)
            driver.find_element_by_id("cmbMunicipio_I").click()
            time.sleep(2)

        # Localidad =
            print("-- Intruduciendo Localidad")
            driver.find_element_by_id("cmbLocalidad_I").clear()
            time.sleep(1)
            driver.find_element_by_id("cmbLocalidad_I").send_keys("Benito Juarez")
            time.sleep(2)
            driver.find_element_by_id("cmbLocalidad_L_LBI0LBL").click()
            time.sleep(2)
        #colonia =
            print("-- Intruduciendo Colonia")
            driver.find_element_by_id("cmbColonia_I").click()
            time.sleep(1)
            driver.find_element_by_id("cmbColonia_I").click()
            time.sleep(1)
            driver.find_element_by_xpath("//input[@id='cmbColonia_I']").send_keys("VERTIZ NARVARTE")
            time.sleep(1)
            driver.find_element_by_xpath("//input[@id='cmbColonia_I']").click()
            time.sleep(1)
        # Calle
            #print("Intruduciendo Calle")
            #driver.find_element_by_id("cmbCalleUnica").click()
            #time.sleep(1)
            #driver.find_element_by_xpath("//entrada[@id='cmbCalleUnica_I']").send_keys("XOCHICALCO")
            #time.sleep(1)
            #driver.find_element_by_xpath("//entrada[@id='cmbCalleUnica_I']").click()
            #time.sleep(1)

            buscar = driver.find_element_by_xpath("//*[@id='default-tab-1']/div[9]/div[1]").click()
            time.sleep(1)

            # Primera opcion
            ubicacion = driver.find_element_by_xpath("//*[@id='BootstrapGridBusquedaPuntual_DXDataRow0']/td[2]/a").click()
            driver.switch_to.default_content()
            time.sleep(3)
                
            i +=1

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
