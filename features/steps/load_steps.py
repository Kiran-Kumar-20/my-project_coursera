from behave import given
from app import products

@given('the following products')
def step_impl(context):
    for row in context.table:
        product = {
            "name": row["name"],
            "category": row["category"],
            "price": float(row["price"]),
            "availability": row["availability"].lower() == "true"
        }
        products.append(product)
