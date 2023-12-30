import json

from flask import Flask, jsonify, request
from kafka import KafkaProducer;

#Initialize app variable

app = Flask(__name__); # Initialize flask


transactionProducer = KafkaProducer(
                                    #bootstrap_servers =['broker:9092'],
                                    value_serializer=lambda m:json.dumps(m).encode('ascii'),
                                    retries=5);


def on_send_success(record_metadata):

    print (record_metadata.topic)

    print (record_metadata.partition)

    print (record_metadata.offset)




def on_send_error(excp):

    # log.error('I am an errback', exc_info=excp)

    print ('There was an error with sending: {}'.format(excp))

@app.route("/transactionGenerator/api", methods=['POST'])
def home():
    jsonData = request.get_json();
    print(f"The Json Data sent==",jsonData);
    transactionProducer.send("financial_transaction",jsonData);
    transactionProducer.flush();
    resp ={"status":200,"msg":"Successfull","data":jsonData};
    return jsonify(resp);
    #return "This is my home attached to the root url /. You get it?";

@app.route("/hello", methods=['GET'])
def hello():
    data = {"data":"Hello World from Transaction Generator API!!"}
    return jsonify(data);




if __name__  == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True);


