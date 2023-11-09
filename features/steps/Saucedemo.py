from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que eu esteja na tela de login da Saucedemo')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com")

@when('preencher com meus dados e clicar no botão "Login"')
def step_impl(context):
    username = context.driver.find_element(By.ID, 'user-name')
    password = context.driver.find_element(By.ID, 'password')
    login_button = context.driver.find_element(By.ID, 'login-button')

    username.send_keys("admin")
    password.send_keys("admin")
    login_button.click()

@then('não conseguirei acessar a pagina')
def step_impl(context):
    error_message = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
    )
    assert "Epic sadface: Username and password do not match any user in this service" in error_message.text

    context.driver.quit()