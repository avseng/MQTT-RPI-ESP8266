import network
from umqtt.simple import MQTTClient
from machine import Pin
from time import sleep


MQTT_SERVER = "192.168.29.230"
CLIENT_ID = "esp_cleint1"
MQTT_TOPIC = b"TEST"
WIFI_SSID = "NETGEAR69"
WIFI_PASSWORD = "unevenlake013"

led = Pin(2, Pin.OUT)

# WiFi connectivity function.
def connectWIFI():
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.connect(WIFI_SSID,WIFI_PASSWORD)
  while not wlan.isconnected():
    pass

  print ("wifi connected")  
  print(wlan.ifconfig())
  
  
#MQTT callback service function
def sub_cb(topic, msg): 
  print(topic, msg)
  if topic.decode() == MQTT_TOPIC.decode() and msg.decode() == 'ON':
    led.value(0)
    print("LED is ON")
  if topic.decode() == MQTT_TOPIC.decode() and msg.decode() == 'OFF':
    led.value(1)
    print("LED is OFF")

 
try:
  led.value(1)
    
  connectWIFI()
  c = MQTTClient(CLIENT_ID,MQTT_SERVER)
  c.set_callback(sub_cb)
  c.connect()
  c.subscribe(MQTT_TOPIC)
  
  print("MQTT connected and ready to receive message")
  while True:
    c.wait_msg()
finally:
  c.disconnect()