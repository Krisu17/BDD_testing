from behave import *
from email_validator import email_validator

@given("{email} as a Email")
def step_impl(context, email):
    context.email = email

@when("I test validity of Email")
def step_impl(context):
    context.returnedValue = email_validator(context.email)

@then("I get {returnedValue} in return")
def step_impl(context, returnedValue):
    assert context.returnedValue == returnedValue