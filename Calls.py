class Subscriber:
    def __init__(self, name: str, inn: str, account: str, phone: str):
        self.__name = name
        self.__inn = inn
        self.__account = account
        self.__phone = phone
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__validate_name(value)
        self.__name = value

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        self.__validate_inn(value)
        self.__inn = value

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value: str):
        self.__validate_account(value)
        self.__account = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value: str):
        self.__validate_phone(value)
        self.__phone = value

    @staticmethod
    def __validate_name(value: str):
        if not value or not value.strip():
            raise ValueError("Имя не может быть пустым.")
    
    @staticmethod
    def __validate_inn(value: str):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("ИНН должен быть строкой из 10 цифр.")
    
    @staticmethod
    def __validate_account(value: str):
        if not value.isdigit() or len(value) < 20:
            raise ValueError("Банковский счет должен быть строкой из 20 цифр.")
    
    @staticmethod
    def __validate_phone(value: str):
        if not value.isdigit() or len(value) < 11:
            raise ValueError("Телефон должен быть строкой из 11 цифр.")
