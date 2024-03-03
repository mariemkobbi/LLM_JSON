import paho.mqtt.client as mqtt
import json
import time
import os
from LLM_JSON import result

# broker address and topic
broker_address = "mqtt.eclipseprojects.io"
topic = "Spirulina_Edge"


# Create an MQTT client
client = mqtt.Client()

# Connect to the broker
client.connect(broker_address)

while True:

    # Publish the message
    print("Published data:")
    client.publish(topic, json.dumps(result))
    print( result)

    # Sleep for 30 minutes
    time.sleep(2)

# Disconnect from the broker 
client.disconnect()



