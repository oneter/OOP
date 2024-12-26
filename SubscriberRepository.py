import yaml
import json
import os
from Subscriber import Subscriber
from BriefSubscriber import BriefSubscriber
from SubscriberRepFileStrategy import SubscriberRepFileStrategy

class SubscriberRepository:

    def __init__(self, strategy: SubscriberRepFileStrategy):
        self.strategy = strategy

    def get_all(self):
        return [Subscriber.from_dict(item) for item in self.strategy.read()]

    def save_all(self, subscribers):
        self.strategy.write([subscriber.to_dict() for subscriber in subscribers])

    def get_by_id(self, subscriber_id):
        subscribers = self.get_all()
        for subscriber in subscribers:
            if subscriber.subscriber_id == subscriber_id:
                return subscriber
        return None

    def get_k_n_short_list(self, k, n):
        subscribers = self.get_all()
        start_index = k * n
        end_index = start_index + n
        return subscribers[start_index:end_index]

    def sort_by_field(self, field):
        subscribers = self.get_all()
        subscribers.sort(key=lambda x: getattr(x, field))
        self.save_all(subscribers)

    def add_subscriber(self, name, inn, account, phone):
        subscribers = self.get_all()
        new_id = max((subscriber.subscriber_id for subscriber in subscribers), default=0) + 1
        new_subscriber = Subscriber(new_id, name, inn, account, phone)
        subscribers.append(new_subscriber)
        self.save_all(subscribers)
        return new_subscriber

    def update_subscriber(self, subscriber_id, name=None, inn=None, account=None, phone=None):
        subscribers = self.get_all()
        for subscriber in subscribers:
            if subscriber.subscriber_id == subscriber_id:
                if name is not None:
                    subscriber.name = name
                if inn is not None:
                    subscriber.inn = inn
                if account is not None:
                    subscriber.account = account
                if phone is not None:
                    subscriber.phone = phone
                self.save_all(subscribers)
                return subscriber
        return None

    def delete_subscriber(self, subscriber_id):
        subscribers = self.get_all()
        subscribers = [subscriber for subscriber in subscribers if subscriber.subscriber_id != subscriber_id]
        self.save_all(subscribers)

    def get_count(self):
        return len(self.get_all())

