import paho.mqtt.client as mqtt
import random
import json  
import datetime 
import time



def on_publish():
    client = mqtt.Client()
    client.username_pw_set("6EgzoIzoGVQR1dWXyfpS","xxxx")
    client.connect('thingsboard.cloud', 1883, 60)
    payload = {'ExhaustGas_Airflow' : random.uniform(1, 10),
               'ExhaustGas_SOx' : random.uniform(1, 10),
               'ExhaustGas_O2' : random.uniform(1, 100),
               'ExhaustGas_NOx' : random.uniform(1, 10), 
               'ExhaustGas_HCl' : random.uniform(1, 10),
               'ExhaustGas_MC' : random.uniform(1, 10),
               'ExhaustGas_CO' : random.uniform(1, 10)
                 }
    print (json.dumps(payload))
    client.publish("v1/devices/me/telemetry", json.dumps(payload))
    time.sleep(1)


while True:
    
    on_publish()

    time.sleep(600)
