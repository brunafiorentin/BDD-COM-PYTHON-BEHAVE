from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('que eu esteja no site da Magazine Luiza')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.magazineluiza.com.br/")

@when('procurar por um produto no campo de pesquisa')
def step_impl(context):
    search_input = context.driver.find_element(By.ID, 'input-search')
    search_input.send_keys("Mesa")
    search_input.submit()

@then('ao clicar no produto pesquisado serei direcionada para a página de resultados da busca')
def step_impl(context):
    assert "Magazine Luiza | Pra você é Magalu!" in context.driver.title


    context.driver.quit()



