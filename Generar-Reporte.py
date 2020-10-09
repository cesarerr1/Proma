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

    def test_Incidentes_Por_Tiempo(self):
        driver = self.driver
        driver.get("http://qa-promad.opensystems.mx/")
        wait = WebDriverWait(driver, 30)
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
        driver.find_element_by_id("icnPlaneacion").click()
        time.sleep(10)
    #FECHA INICIAL

        driver.find_element_by_css_selector("body>app-root>app-dashboard>div>div.ml-3>app-estadisticos>app-tiempo>app-filters-reports>div>div:nth-child(1)>div.d-flex.align-items-center.justify-content-between>app-datepicker:nth-child(1)>div>span>fa-icon").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#mat-datepicker-0>mat-calendar-header>div>div>button.mat-calendar-period-button.mat-button").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#mat-datepicker-0>div>mat-multi-year-view>table>tbody>tr:nth-child(2)>td.mat-calendar-body-cell.mat-calendar-body-active.ng-star-inserted>div").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#mat-datepicker-0>div>mat-year-view>table>tbody>tr:nth-child(2)>td:nth-child(1)").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#mat-datepicker-0>div>mat-month-view>table>tbody>tr:nth-child(1)>td:nth-child(3)").click()
        time.sleep(1)
    #FECHA FINAL
        driver.find_element_by_css_selector(
            "body>app-root>app-dashboard>div>div.ml-3>app-estadisticos>app-tiempo>app-filters-reports>div>div:nth-child(1)>div.d-flex.align-items-center.justify-content-between>app-datepicker.ml-3>div>span>fa-icon").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='mat-datepicker-1']/div/mat-month-view/table/tbody/tr[4]/td[5]").click()
        time.sleep(1)
    #







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
