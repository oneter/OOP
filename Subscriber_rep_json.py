import json
import os
from Subscriber import Subscriber
from decimal import Decimal
from SubscriberRepository import SubscriberRepository
from SubscriberRepositoryStrategy import SubscriberRepFileStrategy

class JsonSubscriberRepFileStrategy(SubscriberRepFileStrategy):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def write(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def display(self):
        data = self.read()
        for item in data:
            print(item)

# Определяем путь к файлу JSON
strategy = JsonSubscriberRepFileStrategy('subscribers.json')


# Создание репозитория с использованием стратегии JSON
json_repository = SubscriberRepository(strategy)

new_subscriber = Subscriber.create_new_subscriber(
    product_id= 3,
    name="Продук",
    description="Описание продукта",
    price=Decimal('19.99'),
    stock_quantity=100,
    material="Пластик",
    product_code="5890000"
)

for subscriber in json_repository.get_k_n_short_list(1,1):
    print(subscriber)


# Отображение обновленного списка продуктов
print("\nUpdated products in JSON file:")
strategy.display()
