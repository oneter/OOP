from SubscriberRepository import  SubscriberRepository

class SubscriberRepositoryAdapter:

    def __init__(self, subscriber_repository: SubscriberRepository):
        self._subscriber_repository = subscriber_repository

    def get_k_n_short_list(self, k, n):
        return self._subscriber_repository.get_k_n_short_list(k, n)

    def get_by_id(self, subscriber_id):
        return self._subscriber_repository.get_by_id(subscriber_id)

    def delete_by_id(self, subscriber_id):
        self._subscriber_repository.subscriber_delete_by_id(subscriber_id)
        self._subscriber_repository.write_data()

    def update_by_id(self, subscriber_id, name, phone, inn, account):
        self._subscriber_repository.subscriber_replace_by_id(subscriber_id, name, phone, inn, account)
        self._subscriber_repository.write_data()

    def add(self, subscriber):
        self._subscriber_repository.add_subscriber(subscriber)
        self._subscriber_repository.write_data()

    def get_count(self):
        return self._subscriber_repository.get_count()
