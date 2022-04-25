import random  
import time  
  
from azure.iot.device import IoTHubDeviceClient, Message
from azure.iot.device.common.auth.connection_string import DEVICE_ID  
  
CONNECTION_STRING = "HostName=southindia-iothub-grp14-2204.azure-devices.net;DeviceId=myiotDevice;SharedAccessKey=TXNEj06Z/T2USKfNZNvrjRhuQpjT4KcaGsSYwvV7xJk="  
global DEVICEID  
TEMPERATURE = 20.0  
HUMIDITY = 60  
MSG_TXT = '{{"deviceId": "{deviceid}", "temperature": {temperature},"humidity": {humidity}}}'  
  
def iothub_client_init():  
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)  
    return client  
  
def iothub_client_telemetry_sample_run():  
  
    try:  
        client = iothub_client_init()  
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )  
        while True:  
            
            temperature = TEMPERATURE + (random.random() * 15)  
            humidity = HUMIDITY + (random.random() * 20)  
            deviceid = "myiotDevice"
            msg_txt_formatted = MSG_TXT.format(deviceid=deviceid,temperature=temperature, humidity=humidity)  
            message = Message(msg_txt_formatted)  
  
            #if temperature > 30:  
            #  message.custom_properties["temperatureAlert"] = "true"  
            #else:  
            #  message.custom_properties["temperatureAlert"] = "false"  
  
            print( "Sending message: {}".format(message) )  
            client.send_message(message)  
            print ( "Message successfully sent" )  
            time.sleep(3)  
  
    except KeyboardInterrupt:  
        print ( "IoTHubClient sample stopped" )  
  
if __name__ == '__main__':  
    print ( "IoT Hub Quickstart #1 - Simulated device" )  
    print ( "Press Ctrl-C to exit" )  
    iothub_client_telemetry_sample_run()
