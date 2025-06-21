### Kafka demo app
Inspired by this [playlist](https://www.youtube.com/watch?v=vD9Ic8KqEDw&list=PL2UmzTIzxgL7Bq-mW--vtsM2YFF9GqhVB&index=9)

### Create a cluster and start server
```sh
KAFKA_CLUSTER_ID="tutysaras-kafka-cluster"
bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c config/server.properties
bin/kafka-server-start.sh config/server.properties
```

### Create topic

```sh
# create a test topic
bin/kafka-topics.sh --create --topic tbus-data --bootstrap-server localhost:9092
bin/kafka-topics.sh --describe --topic tbus-data --bootstrap-server localhost:9092

```
### Test send to topic

```sh
bin/kafka-console-producer.sh --topic tbus-data --bootstrap-server localhost:9092
```

### Test read from topic
```sh
bin/kafka-console-consumer.sh --topic tbus-data --from-beginning --bootstrap-server localhost:9092
```


#### Install monitoring scripts
```sh
uv pip install 'glances[web]''
```
