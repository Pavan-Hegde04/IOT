from asyncio import events
import time
import os
import threading
import subprocess
from subprocess import call
from azure.iot.device import IoTHubDeviceClient

RECEIVED_MESSAGES = 0

CONNECTION_STRING = "HostName=myiothub2404.azure-devices.net;DeviceId=myIotdevice14;SharedAccessKey=egnLk6FK9tgDDFvI7HKOFv9Jn7JrjPOUvA9cPAfoRrI="

global event
event = 0

def play1():
    call("mplayer /home/pavan/Training/IOT/Day4/Marvel.mp3", shell=True)

def play2():
    call("mplayer /home/pavan/Training/IOT/Day4/Moon_Knight.mp3", shell=True)


def message_handler(message):
    global RECEIVED_MESSAGES
    RECEIVED_MESSAGES += 1
    print("")
    print("Message received:")

    # print data from both system and application (custom) properties

    for i in vars(message).items():

        if(i[1]==b'1'):

            # print("yes")

            os.system("gedit file1.txt")

        if(i[1]==b'2'):

            # print("yes")

            t1 = threading.Thread(target=play1)

            t2 = threading.Thread(target=play2)

            t1.start()

            # starting thread 2

            t2.start()

            t1.join()

            # wait until thread 2 is completely executed

            t2.join()

    # print data from both system and application (custom) properties
    for property in vars(message).items():
        print ("    {}".format(property))

    print("Total calls received: {}".format(RECEIVED_MESSAGES))

def main():
    print ("Starting the Python IoT Hub C2D Messaging device sample...")

    # Instantiate the client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    print ("Waiting for C2D messages, press Ctrl-C to exit")
    try:
        # Attach the handler to the client
        client.on_message_received = message_handler

        while True:
            time.sleep(1000)
    except KeyboardInterrupt:
        print("IoT Hub C2D Messaging device sample stopped")
    finally:
        # Graceful exit
        print("Shutting down IoT Hub Client")
        client.shutdown()

if __name__ == '__main__':
    main()
