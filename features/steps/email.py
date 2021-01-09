from behave import *
from email_validator import email_validator

@given("{email} as a Email")
def step_impl(context, email):
    context.email = email

@when("validate Email")
def step_impl(context):
    context.returnedValue = email_validator(context.email)

@then("receive {returnedValue} in return Email test")
def step_impl(context, returnedValue):
    assert context.returnedValue == returnedValue