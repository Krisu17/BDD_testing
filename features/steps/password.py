from behave import *
from password_validator import validate

@given("{email} as a Password")
def step_impl(context, email):
    context.email = email

@when("validate Password")
def step_impl(context):
    context.returnedValue = validate(context.email)

@then("receive {returnedValue} in return Password test")
def step_impl(context, returnedValue):
    assert context.returnedValue == returnedValue