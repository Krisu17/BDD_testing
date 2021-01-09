from behave import *
from entrophy_validator import returnEnthrophyLevel

@given("{entrophy} as a Entrophy")
def step_impl(context, entrophy):
    context.entrophy = entrophy

@when("validate Entrophy")
def step_impl(context):
    context.returnedValue = returnEnthrophyLevel(context.entrophy)

@then("receive {returnedValue} in return Entrophy test")
def step_impl(context, returnedValue):
    assert context.returnedValue == returnedValue