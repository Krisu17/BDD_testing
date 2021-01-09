from behave import *
from login_valdiator import checkLogin

@given("{login} as a Login")
def step_impl(context, login):
    context.login = login

@when("validate Login")
def step_impl(context):
    context.returnedValue = checkLogin(context.login)

@then("receive {returnedValue} in return Login test")
def step_impl(context, returnedValue):
    assert context.returnedValue == returnedValue
