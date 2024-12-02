import json
from decimal import Decimal
from datetime import date


class BriefSubscriber:
    """Класс для краткой информации об абоненте."""

    def __init__(self, subscriber_id: int = 0, name: str, phone: str):
        self.subscriber_id = subscriber_id
        self.name = name
        self.phone = phone

    def __eq__(self, other):
        if not isinstance(other, BriefSubscriber):
            return False
        return (
            self.subscriber_id == other.subscriber_id and
            self.name == other.name and
            self.phone == other.phone
        )

    def __hash__(self):
        return hash((self.subscriber_id, self.name, self.phone))

    def __str__(self):
        return f"BriefSubscriber(subscriberId={self.subscriber_id}, name='{self.name}', phone='{self.phone}')"


class Subscriber(BriefSubscriber):
    """Класс для полной информации об абоненте."""

    def __init__(
        self,
        subscriber_id: int = 0,
        name: str = "",
        inn: str = "",
        account: str = "",
        phone: str = ""
    ):
        super().__init__(subscriber_id, name, phone)
        self.inn = inn
        self.account = account

    # Геттеры и сеттеры с валидацией
    @property
    def inn(self):
        return self._inn

    @inn.setter
    def inn(self, value: str):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("ИНН должен содержать 10 цифр.")
        self._inn = value

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value: str):
        if not value.isdigit() or len(value) < 10:
            raise ValueError("Номер счета должен содержать не менее 10 цифр.")
        self._account = value

    # Методы создания объектов
    @classmethod
    def create_new_subscriber(cls, name: str, inn: str, account: str, phone: str):
        return cls(name=name, inn=inn, account=account, phone=phone)

    @classmethod
    def create_from_json(cls, json_string: str):
        data = json.loads(json_string)
        return cls(
            subscriber_id=data.get("subscriber_id", 0),
            name=data["name"],
            inn=data["inn"],
            account=data["account"],
            phone=data["phone"]
        )

    def to_json(self) -> str:
        return json.dumps({
            "subscriber_id": self.subscriber_id,
            "name": self.name,
            "inn": self.inn,
            "account": self.account,
            "phone": self.phone
        }, ensure_ascii=False)

    def __str__(self):
        return (f"Subscriber(subscriberId={self.subscriber_id}, name='{self.name}', inn='{self.inn}', "
                f"account='{self.account}', phone='{self.phone}')")


if __name__ == "__main__":
    try:
        # Создаем абонента
        subscriber = Subscriber.create_new_subscriber(
            name="ООО Ромашка",
            inn="1234567890",
            account="123456789012",
            phone="89001234567"
        )

        print(subscriber)

        # из JSON
        subscriber_from_json = Subscriber.create_from_json(
            '{"subscriber_id": 1, "name": "ООО Василек", "phone": "89003456789", "inn": "1122334455", "account": "556677889900"}'
        )
        print(subscriber_from_json)

        # JSON представлениe объекта
        print(subscriber.to_json())


    except ValueError as e:
        print("Error:", e)
