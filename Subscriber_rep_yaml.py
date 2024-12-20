import os
import yaml
from decimal import Decimal
from SubscriberRepository import SubscriberRepository
from SubscriberRepositoryStrategy import SubscriberRepFileStrategy
from Subscriber import Subscriber  # Импортируем класс Subscriber

class YamlSubscriberRepFileStrategy(SubscriberRepFileStrategy):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file) or []

    def write(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, allow_unicode=True, default_flow_style=False)

    def add(self, subscriber):
        data = self.read()
        data.append(subscriber.to_dict())
        self.write(data)

    def display(self):
        data = self.read()
        for item in data:
            print(item)

# Инициализация стратегии YAML
strategy = YamlSubscriberRepFileStrategy('subscribers.yaml')

# Чтение данных из файла и отображение их
print("Current subscribers in YAML file:")
strategy.display()

# Создание репозитория с использованием стратегии YAML
yaml_repository = SubscriberRepository(strategy)

# Создание нового продукта
new_subscriber = Subscriber.create_new_product(
    product_id= 3,
    name="Продук",
    description="Описание продукта",
    price=Decimal('19.99'),
    stock_quantity=100,
    material="Пластик",
    product_code="5890000"
)


yaml_repository.add_subscriber(new_subscriber)

yaml_repository.write_data()

# Отображение обновленного списка продуктов
print("\nUpdated subscribers in YAML file:")
strategy.display()
