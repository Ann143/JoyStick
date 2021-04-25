from microbit import *
import paho.mqtt.client as mqtt
blank = Image("00000:"    #this displays no image on microbit
             "00000:"
             "00000:"
             "00000:"
             "00000")
def on_connect(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    if rc == 0:
        display.show(Image.YES)
        client.subscribe("signalpointer") #this the topic

def on_message(client, userdata, msg):
    # print(msg.topic+" "+msg.payload.decode())
    if msg.topic == "signalpointer":                  #the topic 
        if msg.payload.decode() == "C":               #if the payload is equal to C
            display.show(blank)                       #it displays no image
        elif msg.payload.decode() == "N":             #if the payload is equal to N
            display.show(Image.ARROW_N)               #it displays the arrow pointing north
        elif msg.payload.decode() == "NE":            #if the payload is equal to NE
            display.show(Image.ARROW_NE)              #it displays the arrow pointing North East
        elif msg.payload.decode() == "NW":            #if the payload is equal to NW
            display.show(Image.ARROW_NW)              #it displays the arrow pointing North West
        elif msg.payload.decode() == "S":             #if the payload is equal to South
            display.show(Image.ARROW_S)               #it displays the arrow pointing to South
        elif msg.payload.decode() == "SE":            #The process of the rest are the same above.
            display.show(Image.ARROW_SE)
        elif msg.payload.decode() == "SW":
            display.show(Image.ARROW_SW)
        elif msg.payload.decode() == "W":
            display.show(Image.ARROW_W)
        elif msg.payload.decode() == "E":
            display.show(Image.ARROW_E)
        
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()
