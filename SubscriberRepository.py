from typing import List, Optional
from decimal import Decimal
from Subscriber import Subscriber
from BriefSubscriber import BriefSubscriber
from SubscriberRepositoryStrategy import SubscriberRepFileStrategy


class SubscriberRepository:
    def __init__(self, strategy: SubscriberRepFileStrategy):
        self._data = []
        self._strategy = strategy
        self.read_data()

    def write_data(self):
        self._strategy.write(self._data)

    def read_data(self):
        self._data = self._strategy.read()

    def add_subscriber(self, subscriber: Subscriber):
        subscriber_dict = subscriber.to_dict()
        subscribers = [Subscriber.create_from_dict(sub) for sub in self._data]
        if not self.check_unique_code(subscriber, subscribers):
            raise ValueError(f"Subscriber already exists.")
        self._data.append(subscriber_dict)

    def check_unique_code(self, subscriber, subscribers):
        for subscriber_data in subscribers:
            if subscriber_data == subscriber:
                raise ValueError(f"Subscriber already exists.")
        return True

    def get_by_id(self, subscriber_id: int) -> Optional[Subscriber]:
        for subscriber in self._data:
            if subscriber['subscriber_id'] == subscriber_id:
                return Subscriber.create_from_dict(subscriber)
        return None

    def get_k_n_short_list(self, k: int, n: int) -> List[BriefSubscriber]:
        start_index = (n - 1) * k
        end_index = start_index + k
        return [
            BriefSubscriber(
                subscriber_id=subscriber['subscriber_id'],
                name=subscriber['name'],
                phone=subscriber['phone']
            )
            for subscriber in self._data[start_index:end_index]
        ]

    def sort_by_field(self, field: str, reverse: bool = False) -> List[Subscriber]:
        if field not in ['subscriber_id', 'name', 'phone', 'inn', 'account']:
            raise ValueError(f"Invalid field '{field}' for sorting.")
        self._data.sort(key=lambda x: x.get(field), reverse=reverse)
        return [Subscriber.create_from_dict(subscriber) for subscriber in self._data]

    def subscriber_replace_by_id(self, subscriber_id: int, name=None, phone=None, inn=None, account=None):
        # Получаем данные абонента по ID
        subscriber_data = self.get_by_id(subscriber_id)
        if not subscriber_data:
            raise ValueError(f"Subscriber with ID {subscriber_id} not found.")

        # Создаём объект Subscriber из данных найденного абонента
        subscriber = Subscriber.create_from_dict(subscriber_data)

        # Проверяем уникальность
        if not self.check_unique_code(subscriber.to_dict(), subscriber_data):
            raise ValueError("Subscriber already exists.")

        # Обновляем поля объекта Subscriber
        if name:
            subscriber.name = name
        if phone:
            subscriber.phone = phone
        if inn:
            subscriber.inn = inn
        if account:
            subscriber.account = account

    # Обновляем данные в списке
        for i, s in enumerate(self._data):
            if s['subscriber_id'] == subscriber_id:
                self._data[i] = subscriber.to_dict()
                break

    def subscriber_delete_by_id(self, subscriber_id: int):
        subscriber = self.get_by_id(subscriber_id)
        if not subscriber:
            raise ValueError(f"Subscriber with ID {subscriber_id} not found.")
        self._data = [
            s for s in self._data if s['subscriber_id'] != subscriber_id]

    def get_count(self) -> int:
        return len(self._data)
