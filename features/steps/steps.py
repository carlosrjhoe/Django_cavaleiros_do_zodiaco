from behave import when, given
from selenium.webdriver import Chrome
import time

@given('Dado que esteja na pagina "{page}"')
def open_page(context, page):
    context.driver = Chrome()
    context.driver.get(page)

@when('Quando inserir o "{field}" "{value}"')
def insert_values_on_fields(context, field, value):
    pass