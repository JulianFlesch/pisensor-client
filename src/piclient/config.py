import os

env = os.environ

# device settings
device_name = env.get("PICLIENT_DEVICE_NAME", "Default Client")
installed_sensors = env.get("PICLIENT_SENSORS", "").split("")

# transmission settings
use_mqtt = env.get("PICLIENT_USE_MQTT", "1")
broker_server = env.get("PICLIENT_BROKER", "192.169.0.34")
token = env.get("PICLIENT_TOKEN", "")
user = env.get("PICLIENT_USER", "")
password = env.get("PICLIENT_PASS", "")

# Camera Settings
camera_resolution = env.get("PICLIENT_CAMERA_RES", "1024,768").split(",")
camera_wait = int(env.get("PICLIENT_CAMERA_WAIT_TIME", "5"))
