from lib.mqtt_async import MQTTClient, config
import uasyncio as uasync

config["ssid"] = "Emils Galaxy"
config["wifi_pw"] = "gerp1112"
config['server'] = 'mqtt.iotlab.dev'
config['port'] = 1883
config['user'] = 'king'
config['password'] = 'arthur'
MQTTClient.DEBUG = True

client = MQTTClient(config)



async def conn_handeler(client):
    await client.subscribe("JE/e_status")

async def main(client):
    while True:
        await client.publish("JE/e2_status", "{}".format(temp))

config['subs_cb'] = callback
config['connect_coro'] = conn_handeler

try:
    uasync.run(main(client))
finally:
    client.disconnect()
