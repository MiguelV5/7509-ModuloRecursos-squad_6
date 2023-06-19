from behave import *

@given('soy un usuario')
def step_impl(context):
    pass

@then("recibo un error de no existencia")
def step_impl(context):
    assert context.response.status_code == 404

@then("recibo un error")
def step_impl(context):
    assert context.response.status_code == 400

@then("recibo un error por no completar toda la informacion requerida")
def step_impl(context):
    assert context.response.status_code == 422