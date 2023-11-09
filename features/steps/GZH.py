from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('que eu esteja na página de esportes da GauchaZH')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://gauchazh.clicrbs.com.br/esportes/ultimas-noticias/")

@when('eu clicar na Logo localizada no header da página')
def step_impl(context):
    logo = context.driver.find_element(By.XPATH, '//*[@id="gzh-all"]/div/header/div/div[1]/div/div')
    logo.click()

@then('deverei retornar para a Home')
def step_impl(context):
    assert "https://gauchazh.clicrbs.com.br/" in context.driver.current_url

    context.driver.quit()