# Magic Mirror Led Controller - SERVER
# Created for the GDA production of Beauty and the Beast
# Written by Andrew Farabow

import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server


client_ip = "127.0.0.1"
client_port = 5005


def print_mode(unused_addr, args, volume):
    print("[{0}] ~ {1}".format(args[0], volume))


if __name__ == "__main__":
    dispatcher = dispatcher.Dispatcher()
    # dispatcher.map("/onWhite", print)
    dispatcher.map("/mode", print_mode, "Mode")

    server = osc_server.ThreadingOSCUDPServer((client_ip, client_port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
