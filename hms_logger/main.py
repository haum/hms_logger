import logging
from datetime import datetime

from pymongo import MongoClient
import coloredlogs

from hms_base.client import Client


def get_logger():
    return logging.getLogger(__name__)


def main():
    coloredlogs.install(level='INFO')

    mongo = MongoClient()
    db = mongo['hms']
    collection = db['message_logs']

    c = Client('hms_logger', 'haum', listen_all=True)

    def callback(client, topic, message):
        log_entry = {
            'date': datetime.utcnow(),
            'message': message
        }

        msg_id = collection.insert_one(log_entry).inserted_id
        get_logger().info("Added log entry with id {}".format(msg_id))

    c.listeners.append(callback)
    c.connect()

    try:
        c.start_consuming()
    except KeyboardInterrupt:
        c.stop_consuming()
        c.disconnect()