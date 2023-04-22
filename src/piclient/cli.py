import paho.mqtt.client as mqtt
from paho.mqtt import publish
from .config import Config
from .client import Client as PiClient

def main():
    config = Config()
    pi_client = PiClient(config)

    # TODO: publishers

    # TODO: subscriptions
    # mqtt_client.on_message = pi_client.actor_callback
    # mqtt_client = mqtt.Client(config.device_name)
    # mqtt_client.connect(config.broker, config.port)
    # Looping
    # mqtt_client.loop_forever()        
    
    for topic, data in pi_client.read_all_sensors():
        publish(topic, data, hostname=config.broker)

if __name__ == "main":
    main()
