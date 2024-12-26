from decimal import Decimal
from typing import Optional

class BriefSubscriber:

    def __init__(self, subscriber_id: int = 0, name: str = "", phone: str = ""):
        self.subscriber_id = subscriber_id
        self.name = name
        self.phone = phone

    def __eq__(self, other):
        if not isinstance(other, BriefSubscriber):
            return False
        return (
            self.phone == other.phone
        )

    def __str__(self):
        return f"BriefSubscriber(subscriberId={self.subscriber_id}, name='{self.name}', phone='{self.phone}')"
    

    @property
    def subscriber_id(self) -> int:
        return self.__subscriber_id

    @subscriber_id.setter
    def subscriber_id(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("subscriber_id должен быть неотрицательным числом.")
        self.__subscriber_id = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("Имя не должно быть пустым.")
        self.__name = value

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, value: str):
        if len(value) < 11 or not value.isdigit():
            raise ValueError("Номер телефона должен содержать минимум 11 цифр.")
        self.__phone = value
