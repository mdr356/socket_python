import socket

MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram

class UdpServer:
    def __init__(self) -> None:
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.startServer(self.__sock)

    def startServer(self, sock):
        port = 5001
        hostName = '127.0.0.1' # 'localhost' or ''
        sock.bind((hostName, port))
        self.__startistenning(sock)

    def __startistenning(self, sock):
        print('Socket Listening at {}'.format(sock.getsockname())) # Printing the IP address and port of socket
        
        while True:
            #read the data and client address
            data, clientAddress = sock.recvfrom(MAX_SIZE_BYTES) # Receive at most 65535 bytes at once
            message = data.decode('ascii') #read message
            upperCaseMessage = message.upper() # modify the message

            # print the client ip address and the message
            print('The client at {} says {!r}'.format(clientAddress, message))
            data = upperCaseMessage.encode('ascii')
            
            self.__sendDataTo(sock, data, clientAddress)

    def __sendDataTo(self, sock, data, clientAddress):
        print('send Data back to client')
        sock.sendto(data,clientAddress)


UdpServer()