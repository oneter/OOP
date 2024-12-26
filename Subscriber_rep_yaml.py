import yaml
import os
from Subscriber import Subscriber
from SubscriberRepository import SubscriberRepository
from SubscriberRepFileStrategy import SubscriberRepFileStrategy

class SubscriberRepYamlStrategy(SubscriberRepFileStrategy):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file) or []

    def write(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            yaml.safe_dump(data, file, allow_unicode=True)

    def display(self):
        for item in self.read():
            print(item)
