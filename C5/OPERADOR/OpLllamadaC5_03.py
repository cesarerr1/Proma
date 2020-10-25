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
        host = "http://52.9.236.138:9596"
        driver.get(host)
        now = datetime.now()

        try:
            login = WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.ID, "mat-input-0")))
            archivo_log_tiempos("Cargo login")
        except (RuntimeError, TypeError, NameError):
            archivo_log_tiempos("No cargo login")


        driver.find_element_by_id("mat-input-0").send_keys("DEV02")
        time.sleep(1)
        driver.find_element_by_id("mat-input-1").send_keys("C5")
        time.sleep(1)
        driver.find_element_by_id("mat-input-2").send_keys("12345")
        time.sleep(1)
        driver.find_element_by_class_name("mat-raised-button").click()

        print("termino")


        try:
            bienvenida = WebDriverWait(driver, 30).until(
                EC.visibility_of_all_elements_located((By.ID, "icnAtencion")))
            archivo_log_tiempos("Cargo Bienvenida")
        except (RuntimeError, TypeError, NameError):
            archivo_log_tiempos("No Cargo Bienvenida")


        driver.find_element_by_class_name("icnAtencion").click()
        archivo_log_tiempos("Entrando al CAD")

        #Ciclo Repetitivo
        i = 1
        while i <= 1:
            time.sleep(40)

            driver.find_element_by_id("mat-input-10").send_keys("5525194378")
            time.sleep(1)
            driver.find_element_by_id("mat-input-10").send_keys(Keys.CONTROL + Keys.ENTER)
            time.sleep(2)
            archivo_log_tiempos("Entro la llamada")

            #Ingresando al iframe de la barra de herramientas
            driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='siga']"))
            time.sleep(1)
            print("dentro del iframe")
            driver.find_element_by_id("sidepanelsearchsigacontrol").click()
            time.sleep(2)
            #alcaldia =
            driver.find_element_by_id("cmbMunicipio_I").click()
            time.sleep(2)

            #colonia
            driver.find_element_by_id("cmbColonia_I").send_keys("SAN MARTIN XOCHINAHUAC")
            print("Buscando la colonia")
            time.sleep(2)
            driver.find_element_by_id("cmbColonia_L").click()
            time.sleep(2)

            #buscar
            print("buscar")
            driver.find_element_by_xpath("//a[@class='btn btn-default btn-block text-white clean-button'][contains(.,'Buscar')]").click()
            print("buscar 2")
            #driver.find_element_by_xpath("//html/body/form/div[3]/div[4]/div/div/div[9]/div/a").click()
            time.sleep(2)

            #Primera opcion
            ubicacion = driver.find_element_by_xpath("//*[@id='BootstrapGridBusquedaPuntual_DXDataRow0']/td[2]/a").click()
            driver.switch_to.default_content()
            time.sleep(3)

            #Ventana emergente
            aceptarModal = driver.find_element_by_xpath("//span[@class='mat-button-wrapper'][contains(.,'Aceptar')]").is_displayed()
            print("modal ventana")
            print(aceptarModal)
            driver.find_element_by_xpath("//span[@class='mat-button-wrapper'][contains(.,'Aceptar')]").click()

            #if aceptarModal == "True":
             #   driver.find_element_by_xpath("//span[@class='mat-button-wrapper'][contains(.,'Aceptar')]").click()

            #catalogoclave
            driver.find_element_by_xpath("/html/body/app-root/app-home-operador/div/div[2]/div[3]/app-crear-evento/div/form/div[3]/div/app-select-search/mat-form-field/div/div[1]/div[3]").click()
            print("abrio el catalogo")
            time.sleep(3)
            # print(evencercano.is_displayed())

            #Abandono animal
            driver.find_element_by_xpath("//span[@class='mat-option-text'][contains(text(),'ABANDONO-ANIMAL')]").click()
            time.sleep(2)

            #***PDF
            #driver.find_element_by_xpath("//mat-icon[@class='botton-text mat-icon notranslate material-icons mat-icon-no-color']").click()
            #time.sleep(3)
            #pdf = driver.switch_to.window(driver.window_handles[1])
            #print("Dentro del pdf")
            #if pdf is not None:
                #print("No tenemos PDF")
            #time.sleep(3)
            #driver.close()
            #driver.switch_to.default_content()
            #time.sleep(5)
            #driver.quit()

            #Descripcion del incidente
            driver.find_element_by_xpath("//span[contains(text(),'ENVIAR A DESPACHO')]").click()
            time.sleep(3)
            print("Btn enviar a despacho")

            #PersonsaInvolucradas
            print("incia personas")
            driver.find_element_by_xpath("//div[@class='grid contendor3Columnas contenedor-altura-maxima']//button[1]//span[1]//img[1]").click()
            time.sleep(4)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(4)
            TipoPersona = driver.find_element_by_xpath("//mat-select[@id='mat-select-0']//div[@class='mat-select-arrow']").click()
            if TipoPersona is not None:
                print("Tipo de persona seleccionada" + TipoPersona)
            TipoPersonaSelec = driver.find_element_by_xpath("//span[@class='mat-option-text'][contains(text(),'VÍCTIMA')]").click()
            driver.find_element_by_xpath("//span[contains(text(),'Agregar')]").click()
            time.sleep(3)
            #driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/mat-option[2]/span").click()
            driver.close()
            time.sleep(4)
            print("termona personas")
            driver.switch_to.window(driver.window_handles[0])

            #Objeto involucrado
            print("incia objeto")
            #driver.find_element_by_xpath("/html[1]/body[1]/app-my-app[1]/app-home-operador[1]/div[1]/div[2]/div[3]/app-crear-evento[1]/div[1]/form[1]/div[4]/div[2]/div[1]/div[1]/button[4]/span[1]/img[1]").click()
            driver.find_element_by_xpath("//div[@class='grid contendor3Columnas contenedor-altura-maxima']//button[4]//span[1]//img[1]").click()
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(2)
            #Cantidad
            driver.find_element_by_id("mat-input-5").send_keys("50")
            time.sleep(2)
            #ValorEstimado
            driver.find_element_by_id("mat-input-6").send_keys("506")
            time.sleep(2)
            #Descripción
            driver.find_element_by_id("mat-input-4").send_keys("Comentario")
            time.sleep(2)
            #Tipo
            driver.find_element_by_xpath("//mat-select[@id='mat-select-0']//div[@class='mat-select-arrow-wrapper']").click()
            time.sleep(2)
            #Arma de furgo
            driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/mat-option[2]/span[1]").click()
            time.sleep(2)
            #Subtipo
            driver.find_element_by_xpath("//mat-select[@id='mat-select-1']//div[@class='mat-select-arrow']").click()
            time.sleep(2)
            #Ametralladoras
            driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/mat-option[2]/span[1]").click()
            time.sleep(2)
            driver.find_element_by_xpath("//span[contains(text(),'Agregar')]").click()
            time.sleep(3)
            driver.close()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[0])
            print("Objeto Involucrado gaurdado")

            #Vehiculos
            driver.find_element_by_xpath("//div[@class='grid contendor3Columnas contenedor-altura-maxima']//button[2]//span[1]//img[1]").click()
            print("ingreso a al seccion")
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            driver.find_element_by_id("mat-input-22").send_keys("observaciones")
            print("Lleno observaciones")
            #Rol
            driver.find_element_by_xpath("//mat-select[@id='mat-select-0']//div[@class='mat-select-arrow']").click()
            # //span[contains(text(),'ABANDONADO')]
            driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/mat-option[2]/span[1]").click()
            time.sleep(2)
            #TipoVehículo
            driver.find_element_by_xpath("//mat-select[@id='mat-select-1']//div[@class='mat-select-arrow-wrapper']").click()
            time.sleep(2)
            # //mat-option[@id='mat-option-1151']//span[@class='mat-option-text'][contains(text(),'AUTO')]
            driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/mat-option[2]/span[1]").click()
            time.sleep(3)
            driver.find_element_by_xpath("//body//button[2]").click()
            time.sleep(2)
            driver.close()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[0])
            print("Vehículos involucrados registrado")

            #dinero involucrado
            print("Encontrando el icono dinero")
            #driver.find_element_by_xpath("//mat-select[@id='mat-select-0']//div[@class='mat-select-arrow-wrapper']").click()
            driver.find_element_by_xpath("//mat-icon[contains(normalize-space(),'attach_money')]").click()
            #driver.find_element_by_xpath("//mat-icon[@class='mat-icon notranslate material-icons mat-icon-no-color'][contains(.,'attach_money')]").click()
            print("Si encotro el boton")
            #driver.find_element_by_xpath("//div[@class='grid contendor3Columnas contenedor-altura-maxima']//button[5]//span[1]//img[1]").click()
            time.sleep(3)
            #abre la nueva ventana
            print("Abriendo la ventana")
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(3)
            #*Tipo de moneda
            driver.find_element_by_xpath("//div[@class='mat-select-arrow-wrapper']").click()
            time.sleep(2)
            #DOLARES
            #//span[contains(text(),'DOLARES')]
            driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/mat-option[2]/span[1]").click()
            time.sleep(2)
            #Cantidad estimada
            driver.find_element_by_id("mat-input-3").send_keys("500")
            time.sleep(1)
            #Descripción
            driver.find_element_by_id("mat-input-2").send_keys("automatización dinero involucrado")
            time.sleep(1)
            driver.find_element_by_xpath("//span[contains(text(),'Agregar')]").click()
            time.sleep(4)
            driver.close()
            time.sleep(4)
            print("Dinero involucrado registrado")
            driver.switch_to.window(driver.window_handles[0])
            print("regresando al CAD")
            time.sleep(3)

            #Descripciones del incidente
            #Agregando descripcion
            driver.find_element_by_id("mat-input-15").send_keys("DESCRIPCION 123PROBANDO")
            time.sleep(3)
            driver.find_element_by_id("mat-input-15").send_keys(Keys.ENTER)
            time.sleep(4)

            desciption = driver.find_element_by_id("descripcion")

            # obtiene folio
            obtienefolio = driver.find_element_by_class_name("txt-folio")
            if obtienefolio is not None:
                print("Se genero el folio")
            print(obtienefolio.text)

            fecha2 = time.strftime("%H:%M:%S")
            date_stamp = fecha2.replace(" ", "_").replace(":", "_").replace("-", "_")
            file_name = date_stamp + ".png"
            self.driver.save_screenshot(file_name)
            print("img guardada")
            time.sleep(2)

            #Log
            #existearchivo = os.path.isfile("log.txt")
            #log = open("log.txt", "w", encoding="utf-8")
            #log.write("Fecha de generación: " + time.strftime("%d/%m/%y") + "\n" + "Hora de ejecución: " + fecha2 + "\n" + "Folio: " + obtienefolio.text + "\n" + "Descripción: " + "\n" + desciption.text)
            #log.write("\n-------------------------------------------------------\n")
            #log.close()
            #print("Log archivos")
            #archivo_log(fecha2, obtienefolio, desciption)
            #print("Log archivos 202020")
            #print(desciption.text)

            print("Click boton GUARDAR")
            driver.find_element_by_xpath("//span[@class='botton-text'][contains(.,'GUARDAR')]").click()
            print("BTN GUARDAR")

            print("alerta de pantalla")
            #driver.find_element_by_xpath("/html/body/app-my-app/app-home-operador/div/div[2]/div[3]/app-crear-evento/div/div[2]/button/span/span").click()
            time.sleep(4)
            driver.find_element_by_xpath("//span[text()='ACEPTAR']").click()
            #driver.find_element_by_xpath("").click()
            time.sleep(4)

            print("cerrando iframe")
            driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='siga']"))
            time.sleep(2)
            print("regresando al iframe")
            # driver.find_element_by_id("sidepanelsearchsigacontrol").click()
            driver.find_element_by_xpath("//a[@id='sidepanelsearchsigacontrolclosebutton']//i[1]").click()
            print("cerrando iframe")
            driver.switch_to.default_content()

            time.sleep(15)

            print("termino completo")
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
    #testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\crojas\\PycharmProjects\\QAProjects\\estatus'))
