from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import HtmlTestRunner
import unittest, time, re



class UntitledTestCase(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://promad.opensystems.mx:8081/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_ALPES (self):
        driver = self.driver
        driver.get("http://34.226.133.73:9191/")
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

        driver.find_element_by_id("10").click()
        time.sleep(1)

        driver.find_element_by_id("mat-checkbox-75").click()
        time.sleep(1)

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
        # Cambia el controlador a la ventana o pestaña original
        driver.switch_to.window(win_ser_local)
        time.sleep(3)
        #recurso = driver.assertTrue(driver.is_element_present(By.CSS_SELECTOR, "span.dato-unidad"))
        #print("never:", recurso)



        # recurso = driver.find_element_by_css_selector("span.dato-unidad").size() !=0

        #CERRAR SESION
        driver.find_element_by_xpath("//div[6]/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[2]/div/div/div/button/span").click()
        time.sleep(3)



        #USUARIO
        usuario = driver.find_element_by_id("mat-input-3")
        usuario.send_keys("QA05")
        usuario.send_keys(Keys.ENTER)
        time.sleep(1)

        #CENTRO
        centro = driver.find_element_by_id("mat-input-4")
        centro.send_keys("C5")
        centro.send_keys(Keys.ENTER)
        time.sleep(1)

        #PASSWORD
        clave = driver.find_element_by_id("mat-input-5")
        clave.send_keys("12345")
        clave.send_keys(Keys.ENTER)
        time.sleep(1)

        #MENU
        driver.find_element_by_id("icnAtencionTactica").click()
        time.sleep(1)

        driver.find_element_by_id("10").click()
        time.sleep(1)

        driver.find_element_by_id("mat-checkbox-223").click()
        time.sleep(1 )

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
        # Cambia el controlador a la ventana o pestaña original
        driver.switch_to.window(win_ser_local)
        time.sleep(3)
        recurso = driver.find_element_by_css_selector("span.dato-unidad").size() !=0

        #CERRAR SESION
        driver.find_element_by_xpath("//div[6]/span").click()
        driver.find_element_by_xpath("//div[2]/div/div/div/button/span").click()

        #driver.assertTrue(driver.is_element_present(By.CSS_SELECTOR, "span.dato-unidad"))
        #assert element.text == 'Example Domains'
    #def test_PLATEROS(self):
       #  driver = self.driver

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
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/JOSS/PycharmProjects/QACodes/reports'))
