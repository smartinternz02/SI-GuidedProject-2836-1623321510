[6:49 pm, 02/07/2021] Anu: import wiotp.sdk.device
import time
import random
import sys
import string
myConfig = { 
    "identity": {
        "orgId": "3f5ddu",
        "typeId": "iotdevice",
        "deviceId":"2001"
    },
    "auth": {
        "token": "Sindhu@27"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
for  i  in range(1,10):
     name=input("Enter the name :");
     amount= 100
     while True:
        liter_rate= 2
        waterquantity=random.randint(0,10)
        amountdetection =  waterquantity * liter_rate;
        cost =  amount - amountdetection
        amount =  cost
        if(cost > 0):
            myData={'name':name, 'cost':amountdetection,'waterquantity':waterquantity,'amount left':cost}
            client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
            print("Published data Successfully: %s", myData)
            client.commandCallback = myCommandCallback
            time.sleep(2)
        else:
             myData={'Insuffient fund'}
             #client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
             print("Published data Successfully: %s", myData)
             break
             client.commandCallback = myCommandCallback
             time.sleep(2)
client.disconnect()
