from kc import KafkaClient
import threading
from time import sleep
import json

"""
 kafka client, python example
"""

kClient = KafkaClient()
kClient.setup_env(['kafka1:9092', 'kafka2:9092', 'kafka3:9092'])

data = {"I": "have", "network": "problems"}

while True:
    kClient.produce_to_env("testtopic", data)
    print(data)