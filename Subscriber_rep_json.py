import json
import os
from Subscriber import Subscriber
from SubscriberRepository import SubscriberRepository

class SubscriberRepJson(SubscriberRepository):

    def _read_file(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def _write_file(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        self.save_all(subscribers)

    def get_count(self):
        return len(self.get_all())
