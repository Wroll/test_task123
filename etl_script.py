import requests
from my_app.models import User
import time
from faker import Faker
fake = Faker()


class DataGenerator:
    REF_ID = "ebw7f8ay"
    API_TOKEN = "KWZJ-V50N-5GKS-F46U"
    AMOUNT_OF_USERS = 10
    URL = f"https://randomapi.com/api/{REF_ID}?key={API_TOKEN}&results={AMOUNT_OF_USERS}"

    @classmethod
    def _take_data_from_external_api(cls):
        data = requests.get(cls.URL).json()
        return data['results']

    @classmethod
    def upload_to_db(cls):
        # external api can generate max 10 users. To generate 100 users, i had to make a loop
        for _ in range(10):
            test_data = cls._take_data_from_external_api()
            for user in test_data:
                User(name=fake.name_male(), **user).save()
                time.sleep(0.5)

DataGenerator.upload_to_db()
