import json
import os
from Subscriber import Subscriber
from SubscriberRepository import SubscriberRepository
import json
import os
from SubscriberRepFileStrategy import SubscriberRepFileStrategy

class SubscriberRepJsonStrategy(SubscriberRepFileStrategy):
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
        for item in self.read():
            print(item)

