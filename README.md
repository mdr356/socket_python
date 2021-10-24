# socket_python
## Purpose of the Program
- The client will send a line of text to the server.
- The server will receive the data and convert each character to uppercase.
- The server will send the uppercase characters to the client.
- The client will receive and display them on its screen.

create socket
 socket.socket(family, type)
** family **

- AF_INET : This family is used with IPV4 addresses
- AF_INET6 : Another address scheme, IPv6
- AF_UNIX : processes on a system can communicate with each other 

** type **
- SOCK_DGRAM : User Datagram Protocol (UDP)
- SOCK_STREAM : Transmission Control Protocol (TCP