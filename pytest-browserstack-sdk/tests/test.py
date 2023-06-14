import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_example(selenium):
    selenium.get('https://bstackdemo.com/')
    
    # locating product on webpage and getting name of the product
    productText = selenium.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/p').text

    # clicking the 'Add to cart' button
    selenium.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div[4]').click()
    time.sleep(3)

    # waiting until the Cart pane has been displayed on the webpage // CLIQUEO EL BOTON DE MAS
    selenium.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/div/div[4]/div/button[2]').click()

    # locating product in cart and getting name of the product in cart
    productCartText = selenium.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]').text
    time.sleep(3)
    # checking whether product has been added to cart by comparing product name
    assert productCartText == productText

@pytest.fixture
def selenium():
    print("Comienza la prueba")
    driver = webdriver.Chrome()
    yield driver
    print("Termino la prueba")
    driver.quit()
