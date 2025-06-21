from kafka import KafkaProducer
import json
from datetime import datetime
import uuid
import time

### Read coordinates from json
in_file = open("./data/bus1.json")
json_array = json.load(in_file)
coordinates = json_array["features"][0]["geometry"]["coordinates"]
print("coordinates=", coordinates)

### Generate UUID
def generate_uuid():
    return uuid.uuid4()

### Construct the message
BUS_LINE = "001"

def generate_checkpoint(coordinate):
    data = {}
    data["busline"] = BUS_LINE
    print("coordinate=", coordinate)
    data["key"] = data["busline"] + "_" + str(generate_uuid())
    data["timestamp"] = str(datetime.utcnow())
    data["latitude"] = coordinate[1]
    data["longitude"] = coordinate[0]
    message = json.dumps(data)
    print("message=", message)
    return message

### Kafka related methods
TOPIC_NAME = 'tbus-data'
producer = KafkaProducer(bootstrap_servers='localhost:9092')
def send_to_kafka(message):
    producer.send(TOPIC_NAME, message.encode('ascii'))


### Generate Message and Send to Kafka

while True:
    for coordinate in coordinates:
        message = generate_checkpoint(coordinate)
        send_to_kafka(message)
        time.sleep(1)
