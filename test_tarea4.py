from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from pytest import mark
import time

# Abrir navegardor
driver = webdriver.Chrome()

# maximizar pantalla
driver.maximize_window()
#Pagina Para Abrir
driver.get('https://orbi.edu.do/orbi/')

driver.save_screenshot("results/introPage.png") # Capturo imagen



#Prueba HU1
@mark.ui
def test_HU1():
    #loggear
    element_email = driver.find_element(By.CSS_SELECTOR, '#txtNombreUsuario')
    element_email.send_keys('selinexperezp2@gmail.com')

    element_password = driver.find_element(By.CSS_SELECTOR, '#txtContrasena')
    element_password.send_keys('Hola.123456')
    
    driver.save_screenshot("resultado/filledlogin.png") # Capturo imagen
    #loggear click
    driver.find_element(By.CSS_SELECTOR, '#btnSesion').click()
    driver.save_screenshot("resultado/loginComplete.png") # Capturo imagen
    time.sleep(3)
    assert True
    
#Prueba HU2
@mark.ui
def test_HU2():
    # nav search-typeahead

    driver.find_element(By.CSS_SELECTOR,  '#bajar').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '#div-contenido111 > div > div.col-sm-10.col-md-10 > div > div > a').click()

    
    driver.save_screenshot("resultado/buscarR.png") # Capturo imagen
    time.sleep(3)

    assert True

#Prueba HU3
@mark.ui
def test_HU3():

    driver.find_element(By.CSS_SELECTOR, '#div1Inicio > div:nth-child(4) > div > a > span').click() #nav  horario
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, '#nav > li:nth-child(1) > a').click() # inicio
    driver.save_screenshot("resultado/horario.png") # Capturo imagen'
    time.sleep(5)
   

    assert True

#Prueba HU4
@mark.ui
def test_HU4():

    driver.find_element(By.CSS_SELECTOR, '#nav > li:nth-child(2) > a').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#mGestiónDocencia > a').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#mGestiónDocencia > ul > li:nth-child(2) > a').click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, '#nav > li:nth-child(1) > a').click() # inicio
    time.sleep(5)
    

    driver.find_element(By.CSS_SELECTOR, '#nav > li:nth-child(2) > a').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#mGestiónDocencia > a').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#mGestiónDocencia > ul > li:nth-child(5) > a').click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, '#nav > li:nth-child(1) > a').click() # inicio
    time.sleep(5)
    driver.save_screenshot("resultado/consultacalificacion.png") # Capturo imagen
    assert True

#Prueba HU5
@mark.ui
def test_HU5():

    driver.find_element(By.CSS_SELECTOR, '#div-menu > div').click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, 'body > div.fast_confirm > button.fast_confirm_proceed').click()
    time.sleep(2)

    assert True


@mark.ui
def test_pruebafinal():
    time.sleep(4)
    driver.quit()
    assert True

    