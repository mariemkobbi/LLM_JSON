import paho.mqtt.client as mqtt
import json
import time
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
""" 
#this is the Raspberry pi part
import RPI.GPIO as GPIO
GPIO.setmode(gpio.BCM)

GPIO.setup(21,GPIO.IN) #water level sensor 
start_time = time.time()

#read code from arduino to raspberry pi 
ser = serial.Serial('"/dev/ttyACM0', 115200)  


# Read data from serial
data = ser.readline().decode().strip()

# Split the data into individual values
ArdphValue, ArdConductivityValue, ArdTemperatureValue = map(float, data.split(","))

#water level 
levelbassin = 25
capt = GPIO.input(21)
if capt == 1:
time_ex = time.time() - start_time
Water_Level = levelbassin -(time_ex * 0.7)
        
"""
class LLM_PUBLISH:
    def __init__(self):
        # MQTT configuration
        self.broker_address = "mqtt.eclipseprojects.io"
        self.topic = "Spirulina_Edge"

        # Credentials for LLM
        self.api_key = os.environ['OPENAI_API_KEY']

        # Create MQTT client
        self.client = mqtt.Client()
        self.client.connect(self.broker_address)

    def process_sensor_data(self):
        # Replace with RPI sensor values
        ArdTemperatureValue = 5
        ArdphValue = 5
        Water_Level = 5
        ArdConductivityValue = 5
        Camera = 5

        user_input = f"temperature={ArdTemperatureValue};Ph_value={ArdphValue};water_level={Water_Level};conductivity={ArdConductivityValue};brightness={Camera}"

        # Generate JSON using LLM
        result = self.generate_json(user_input)

        # Publish JSON data to MQTT
        self.publish_data(result)

    def generate_json(self, user_input):
        application_prompt = """Make sure that all responses are in json format and the values are float
        DESCRIPTION:
        {user_input}
        """

        llm = ChatOpenAI(
            temperature=0.7,
            max_tokens=500,
            model='gpt-3.5-turbo',
            api_key=self.api_key
        )

        prompt = PromptTemplate(
            input_variables=["user_input"],
            template=application_prompt
        )

        chain = prompt | llm | StrOutputParser()
        result = chain.invoke({"user_input": user_input})
        return result
    

    def publish_data(self, data):
        self.client.publish(self.topic, json.dumps(data))
        print("Published data:", data)
        

    """ def run(self):
        while True:
            self.process_sensor_data()
            time.sleep(5)

# Create and run 
main = LLM_PUBLISH()
main.run() """

while True:
    main = LLM_PUBLISH()
    main.process_sensor_data()
    time.sleep(5)