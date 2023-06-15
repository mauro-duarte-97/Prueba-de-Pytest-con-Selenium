import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from jira import JIRA

def create_jira_issue(summary):
    jira_server = 'https://ifts18mps.atlassian.net/jira/software/projects/MM/boards/1?issueParent=10003'
    jira_username = 'm.e.b.d.0904@ifts18.edu.ar'
    jira_api_token = 'ATATT3xFfGF0_5piTdGTB6C6CA5rlLJOgJ4VCuieqgsv5Z6p6VJfR9jvG9zhMTjkpArkOgUpRphjWSOekXzhj6niZ-_NnPfApfhnh7sNF1w_ob2DQT8my8R8VTpexgQ1YJfA4H_B91-dL0sl0pHspt2V9LM9HABdagntFEmT33Wq0-HYPbAzO1Q=C1B84B26'
    jira = JIRA(server=jira_server, basic_auth=(jira_username, jira_api_token))

    # Crear un nuevo problema en Jira
    issue_dict = {
        'project': {'key': 'MM-5'},  # Reemplaza 'MM' con la clave de tu proyecto en Jira
        'summary': summary,
        'issuetype': {'name': 'Task'}  # Reemplaza 'Bug' con el tipo de problema que deseas crear
    }
    new_issue = jira.create_issue(fields=issue_dict)
    return new_issue

def update_jira_issue(issue, test_result):
    # Agregar un comentario al problema existente en Jira
    comment = f'Prueba de comentarios del Body: {test_result}'
    issue.fields.comment = {'body': comment}
    issue.update()
    print('Updated issue in JIRA, prueba de Update.')

def test_example(selenium):
    selenium.get('https://bstackdemo.com/')
    
    # Localizar el producto en la página web y obtener su nombre
    productText = selenium.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/p').text

    # Hacer clic en el botón 'Add to cart'
    selenium.find_element(By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div[4]').click()
    time.sleep(3)

    # Esperar hasta que se muestre el panel del carrito en la página web
    selenium.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/div/div[4]/div/button[2]').click()

    # Localizar el producto en el carrito y obtener su nombre
    productCartText = selenium.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]').text
    time.sleep(3)

    # Verificar si el producto se ha agregado al carrito comparando los nombres
    assert productCartText == productText

@pytest.fixture
def selenium():
    print("Comienza la prueba")
    driver = webdriver.Chrome()
    yield driver
    print("Termina la prueba")
    driver.quit()
