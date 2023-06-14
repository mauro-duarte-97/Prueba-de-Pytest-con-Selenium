import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def selenium():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_example(selenium):
    selenium.get('https://bstackdemo.com/')

    # Esperar hasta que el elemento de producto esté presente
    product_element = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/p'))
    )
    product_text = product_element.text
    print(product_text)
    # Hacer clic en el botón 'Add to cart'
    add_to_cart_button = WebDriverWait(selenium, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div[4]'))
    )
    add_to_cart_button.click()

    # Esperar hasta que el elemento del carrito esté presente
    cart_element = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]'))
        )
    product_cart_text = cart_element.text
    print(product_cart_text)
    # Verificar si el producto se ha agregado al carrito comparando los nombres del producto
    assert product_cart_text == product_text

