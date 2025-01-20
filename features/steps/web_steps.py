from behave import when, then
import requests

@when('I visit the "{endpoint}" endpoint')
def step_impl(context, endpoint):
    context.response = requests.get(f"http://localhost:5000{endpoint}")

@then('I should see a list of products')
def step_impl(context):
    assert context.response.status_code == 200
    assert len(context.response.json()) > 0

@then('the response status should be "{status_code}"')
def step_impl(context, status_code):
    assert str(context.response.status_code) == status_code
