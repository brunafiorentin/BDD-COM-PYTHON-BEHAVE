from behave import given, when, then
from selenium import webdriver

base_url = "https://www.uol.com.br/esporte/"
xpath = "/html/body/section[1]/div[2]/div/div/div/div[1]/div"


@given(u'que eu acesso a página da UOL Esporte')
def acessar_site(context):
    context.web = webdriver.Chrome()
    context.web.get(base_url)

@when(u'clicar em determinada notícia')
def step_impl(context):
    context.web.find_element("xpath", xpath).click()

@then(u'eu devo ser direcionada para a outra página que apresenta a manchete')
def step_impl(context):
    assert context.web.title is not None

def after_all(context):
    context.web.quit()