from Credentials import *


class BaseManager:
    def __init__(self, db):
        self.db = db

    def execute_query(self, query, params=None):
        try:
            cursor = self.db.get_connection().cursor()
            cursor.execute(query, params)
            self.db.get_connection().commit()
            logger.info("Query executed successfully")
        except Exception as e:
            self.db.get_connection().rollback()  # Откат
            logger.error(f"Query failed due to {e}")
        finally:
            cursor.close()

    def create_table(self, create_table_query):
        try:
            cursor = self.db.get_connection().cursor()
            cursor.execute(create_table_query)
            self.db.get_connection().commit()
        except Exception as e:
            self.db.get_connection().rollback()
            logger.error(f"Table creation failed due to {e}")
        finally:
            cursor.close()

    def drop_table(self, drop_table_query):
        try:
            cursor = self.db.get_connection().cursor()
            cursor.execute(drop_table_query)
            self.db.get_connection().commit()
            logger.info("Table dropped successfully")
        except Exception as e:
            self.db.get_connection().rollback()  # Откат
            logger.error(f"Table drop failed due to {e}")
        finally:
            cursor.close()

    def add_data(self, insert_query, data):
        try:
            cursor = self.db.get_connection().cursor()
            cursor.executemany(insert_query, data)
            self.db.get_connection().commit()
        except Exception as e:
            self.db.get_connection().rollback()  # Откат
            logger.error(f"Data insertion failed due to {e}")
        finally:
            cursor.close()
