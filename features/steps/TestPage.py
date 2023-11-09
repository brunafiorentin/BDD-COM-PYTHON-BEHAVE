from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('que estou na página inicial do EvilTester Test Pages')
def step_given_open_eviltester(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://testpages.eviltester.com/styled/key-click-display-test.html")

@when('eu clico no botão "Index"')
def step_when_click_button(context):
    button_element = context.driver.find_element(By.LINK_TEXT, "Index")
    button_element.click()

@then('a página "Index" é aberta')
def step_then_page_opened(context):
    assert "Web Testing and Automation Practice Application Pages" in context.driver.title

    context.driver.quit()