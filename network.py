import socket
import time

class Network:
    def __init__(self):
        self.client = socket.socket()
        self.server = "192.168.0.101"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

n = Network()
for i in range(5):
  print("Sending message to client")
  print(n.send("Message " + str(i)))
  print("Sleeping for 5 secs")
  time.sleep(5)


