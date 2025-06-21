from flask import Flask, render_template, Response
from kafka import KafkaConsumer

TOPIC_NAME = 'tbus-data'

app = Flask(__name__)

@app.route("/")
def index():
    return(render_template("./index.html"))

@app.route("/topic/<topicname>")
def stream_messages(topicname):
    def events():
        consumer = KafkaConsumer(topicname)
        for msg in consumer:
            yield "data:{0}\n\n".format(str(msg.value, "utf-8"))
    return Response(events(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
