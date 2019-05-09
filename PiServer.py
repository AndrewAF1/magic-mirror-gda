# Magic Mirror Led Controller - SERVER
# Created for the GDA production of Beauty and the Beast
# Written by Andrew Farabow

from pythonosc import dispatcher
from pythonosc import osc_server
import RPi.GPIO as GPIO


client_ip = "192.168.1.133"
client_port = 5005

# pin on the pi to which the LED strip is connected
gpioPin = 25

# setup the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(gpioPin,GPIO.OUT)


#print output
def print_mode(unused_addr, args, mode):
    print("[{0}] ~ {1}".format(args[0], mode))
    if (mode == False):
        print("Mode: Off")
        GPIO.output(gpioPin,False)
    if (mode == True):
        print("Mode: On")
        GPIO.output(gpioPin,True)


if __name__ == "__main__":
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/mode", print_mode, "Mode")

    server = osc_server.ThreadingOSCUDPServer((client_ip, client_port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
