# PiClient

THIS IS WORK IN PROGRESS.

This is the client to used to collect data from a variety of sensors, without individual setup and transmission via mqtt.

## Installation

```
pip install build
python -m build .
pip install dist/<package-with-version>.tar.gz
```

This installs the package, as well as the executable script `piclient` which can be called to perform a collection and update routine.

## Configuration

For configuration see `src/piclient/config.py`.
Environment variables have precedence over config file has precedence over defaults.

The config file should be located at `/etc/raspiclient_config.ini`

## Future work

- Add more sensors:
    * Temperature
    * Light intensity
    * Humidity
- Add actions and build a deamon that runs a loop, constantly checking for actions coming in via MQTT
