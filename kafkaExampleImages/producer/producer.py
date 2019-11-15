from kc import KafkaClient
import threading
from time import sleep
import json

"""
 kafka client, python example
"""

kClient = KafkaClient()
kClient.setup_env(['kafka1:9092', 'kafka2:9092', 'kafka3:9092'])

data = {"test": "data"}

for i in range(10):
    print("pushing")
    kClient.produce_to_env('test.webserver.topic', bytes(
        json.dumps(data).encode('utf-8')))
