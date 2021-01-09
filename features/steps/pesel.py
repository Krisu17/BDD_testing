from behave import *
from pesel_validator import validate


@given("{pesel} as a PESEL")
def step_impl(context, pesel):
    context.pesel = pesel


@when("validate PESEL")
def step_impl(context):
    context.returned_value = validate(context.pesel)


@then("receive {returned_value} in return PESEL test")
def step_impl(context, returned_value):
    assert context.returned_value == returned_value
