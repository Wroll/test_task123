import requests
from my_app.models import User
from faker import Faker

fake = Faker()


class DataGenerator:
    REF_ID = "ebw7f8ay"
    API_TOKEN = "KWZJ-V50N-5GKS-F46U"
    AMOUNT_OF_USERS = 5  # 100
    URL = f"https://randomapi.com/api/{REF_ID}?key={API_TOKEN}&results={AMOUNT_OF_USERS}"

    @classmethod
    def _take_data_from_external_api(cls):
        data = requests.get(cls.URL).json()
        return data['results']

    @classmethod
    def upload_to_db(cls):
        test_data = cls._take_data_from_external_api()
        for user in test_data:
            User(name=fake.name_male(), **user).save()
