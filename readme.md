#How to use

You must have docker and docker composed installaled to run this app. 

##Receiver

To execute the receiver you must run the following command:

```bash
$> docker-compose up receiver
```

You can watch receiver's logs. When a file is received it will be stored as plain XML in received folder with the timestamp on it's name.

##Sender

To execute the sender you must run the following command:

```bash
$> docker-compose up sender
```

This app will read json files inside "to-send" folder, each file will be converted to XML encrypted and sent to receiver.