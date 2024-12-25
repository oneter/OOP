from decimal import Decimal
from typing import List
from Subscriber import Subscriber

class SubscriberRepDB:
    def __init__(self, host, user, password, database, port=3306):
        self.db = DBConnection(host, user, password, database, port).get_connection()

    def get_by_id(self, subscriber_id: int) -> Subscriber:
        with self.db.cursor() as cursor:
            sql = "SELECT * FROM products WHERE subscriber_id = %s"
            cursor.execute(sql, (subscriber_id,))
            result = cursor.fetchone()
            if result:
                return Subscriber(
                    product_id=result['subscriber_id'],
                    name=result['name'],
                    phone=result['phone'],
                    inn=result['inn'],
                    account=result['account']
                )
            return None

    def get_k_n_short_list(self, k: int, n: int) -> List[Subscriber]:
        offset = (n - 1) * k
        with self.db.cursor() as cursor:
            sql = "SELECT subscriber_id, name, phone FROM subscribers LIMIT %s OFFSET %s"
            cursor.execute(sql, (k, offset))
            results = cursor.fetchall()
            return [
                Subscriber(
                    subscriber_id=row['subscriber_id'],
                    name=row['name'],
                    phone=row['phone']
                ) for row in results
            ]

    def add(self, subscriber: Subscriber):
        try:
            query = """
                INSERT INTO subscribers (name, phone, inn, account)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (subscriber.name, subscriber.phone, subscriber.inn, subscriber.account)

            with self.db.cursor() as cursor:
                cursor.execute(query, values)
                self.db.commit()
        except MySQLError as e:
            if e.args[0] == 1062:
                raise ValueError(f"Subscriber with phone number {subscriber.phone} already exists.")
            else:
                raise Exception("An unexpected error occurred while adding the subscriber.")

    def update_by_id(self, subscriber_id: int, subscriber: Subscriber) -> bool:
        with self.db.cursor() as cursor:
            sql = """
                UPDATE subscribers
                SET name = %s, phone = %s, inn = %s, 
                    account = %s
                WHERE phone = %s
            """
            cursor.execute(sql, (
                subscriber.name,
                subscriber.phone,
                subscriber.inn,
                subscriber.account,
                subscriber_id
            ))
            self.db.commit()
            return cursor.rowcount > 0

    def delete_by_id(self, subscriber_id: int) -> bool:
        with self.db.cursor() as cursor:
            sql = "DELETE FROM subscribers WHERE subscriber_id = %s"
            cursor.execute(sql, (subscriber_id,))
            self.db.commit()
            return cursor.rowcount > 0

    def get_count(self) -> int:
        with self.db.cursor() as cursor:
            sql = "SELECT COUNT(*) AS count FROM subscribers"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['count'] if result else 0

    def close(self):
        self.db.close()
