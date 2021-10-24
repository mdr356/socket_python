import socket

MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram

class UdpClient():
    
    def __init__(self) -> None:
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__startClient(self.__sock)

    def __startClient(self, sock):
        print('The OS assigned the address {} to me'.format(sock.getsockname()))
        message = input('Input lowercase sentence:' )
        data = message.encode('ascii')
        self.__sendDataTo(sock, data)

    def __sendDataTo(self, sock, data):
        port = 5001
        hostName = '127.0.0.1' # 'localhost' or ''
        sock.sendto(data, (hostName, port))

        #data received from server
        data, address = sock.recvfrom(MAX_SIZE_BYTES) 
        self.__processDataReceived(data, address)

    def __processDataReceived(self, data, address):
        text = data.decode('ascii')
        print('The server {} replied with {!r}'.format(address, text))

    
UdpClient()