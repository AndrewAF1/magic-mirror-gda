# Magic Mirror Led Controller - CLIENT
# Created for the GDA production of Beauty and the Beast
# Written by Andrew Farabow

import argparse
import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client


if __name__ == "__main__":
    while (True):
        client = udp_client.SimpleUDPClient("127.0.0.1", 5005)
        print("Press 0 for Off, 1 for On (White)")
        selection = input("Enter A Number: ")
        if (selection == "0"):
            client.send_message("/mode", False)
        if (selection == "1"):
            client.send_message("/mode", True)
