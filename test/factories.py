from faker import Faker
import random

fake = Faker()

class ProductFactory:
    @staticmethod
    def create():
        return {
            "name": fake.word(),
            "category": fake.word(),
            "price": round(random.uniform(10, 100), 2),
            "availability": fake.boolean()
        }
