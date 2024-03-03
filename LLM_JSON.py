from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
import os
import json
import time

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
# Replace with actual sensor reading code 
ArdTemperatureValue = 5
ArdphValue = 5
Water_Level = 5
ArdConductivityValue = 5
Camera = 5

while True:
   
    user_input = f"temperature={ArdTemperatureValue};Ph_value={ArdphValue};water_level={Water_Level};conductivity={ArdConductivityValue};brightness={Camera}"
   

    
    # Define the application prompt
    application_prompt ="""Make sure that all reponses are in json format and the values are float
    here is the template file
    
    DESCRIPTION:
    {user_input}
"""

    # Configure LLM instance
    llm = ChatOpenAI(
        temperature=0.7,
        max_tokens=500,
        model='gpt-3.5-turbo',
        api_key=os.environ['OPENAI_API_KEY']
    )

    # Create the prompt template
    prompt = PromptTemplate(
        input_variables=["user_input"],
        template=application_prompt
    )

    # Using LCEL lanchain expression language
    chain = prompt | llm | StrOutputParser()

    # Execute the chain with user input
    result = chain.invoke({"user_input": user_input})

    # Print the generated JSON data 
    print(f"result{result}")

    
    # Write data to JSON file (now with valid JSON structure)
    # with open("sensor_data.json", "w") as json_file:
    #     json.dump( result, json_file, indent=4)

    # Sleep for 5 seconds
    time.sleep(5)  
