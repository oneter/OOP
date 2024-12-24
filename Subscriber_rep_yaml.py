import yaml
import os
from Subscriber import Subscriber
from SubscriberRepository import SubscriberRepository

class SubscriberRepYaml(SubscriberRepository):
    """Класс для работы с Subscriber в формате YAML."""

    def _read_file(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file) or []

    def _write_file(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            yaml.safe_dump(data, file, allow_unicode=True)
