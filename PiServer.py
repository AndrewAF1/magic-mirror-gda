# Magic Mirror Led Controller - SERVER
# Created for the GDA production of Beauty and the Beast
# Written by Andrew Farabow

from pythonosc import dispatcher
from pythonosc import osc_server
#import RPi.GPIO as GPIO


client_ip = "127.0.0.1"
client_port = 5005

GPIO.setmode(GPIO.BOARD)



def print_mode(unused_addr, args, mode):
    print("[{0}] ~ {1}".format(args[0], mode))
    if (mode == "0"):
        print("Mode: Off")
        #GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    if (mode == "1"):
        print("Mode: On")
        #GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)


if __name__ == "__main__":
    dispatcher = dispatcher.Dispatcher()
    # dispatcher.map("/onWhite", print)
    dispatcher.map("/mode", print_mode, "Mode")

    server = osc_server.ThreadingOSCUDPServer((client_ip, client_port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
