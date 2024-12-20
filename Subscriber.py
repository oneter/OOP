import json
import yaml
from decimal import Decimal
from typing import Optional
from datetime import date
from BriefSubscriber import BriefSubscriber



class Subscriber(BriefSubscriber):

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
    
    @classmethod
    def create_from_string(cls, subscriber_string: str):
        parts = subscriber_string.split(",")
        if len(parts) != 6:
            raise ValueError("Invalid subscriber string format. Expected 6 comma-separated values.")
        try:
            return cls(
                subscriber_id=None,
                name=parts[0].strip(),
                phone=parts[1].strip(),
                inn=parts[3].strip(),
                account=parts[4].strip()
            )
        except ValueError as e:
            raise ValueError("Invalid number format in subscriber string.") from e

    @classmethod
    def create_from_dict(cls, data: dict):
        return cls(
            subscriber_id=data.get('subscriber_id'),
            name=data['name'],
            phone=data['phone'],
            inn=data['inn'],
            account=data['account']
        )
    
    @classmethod
    def create_from_yaml(cls, yaml_string: str):
        data = yaml.safe_load(yaml_string)
        return cls(
            subscriber_id=data.get('subscriber_id'),
            name=data['name'],
            phone=data['phone'],
            inn=data['inn'],
            account=data['account']
        )
    
    def to_yaml(self) -> str:
        return yaml.dump({
            'subscriber_id': self.subscriber_id,
            'name': self.name,
            'phone': self.phone,
            'inn': self.inn,
            'account': self.account
        }, allow_unicode=True)

    def to_dict(self) -> dict:
        return {
            "subscriber_id": self.subscriber_id,
            "name": self.name,
            "phone": self.phone,
            "inn": self.inn,
            "account": self.account
        }
    
    def __str__(self):
        return (f"Subscriber(subscriberId={self.subscriber_id}, name='{self.name}', inn='{self.inn}', "
                f"account='{self.account}', phone='{self.phone}')")
