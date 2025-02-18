# 2DT905

## Emil Ulvagården (eu222dq@student.lnu.se)

### Task 1

#### T1-1

DNS or Domain Name System is used to translate domain names to IP addresses.

TCP or Transmission Control Protocol is used to ensure that data delivery between devices are ordered, reliable and error checked.

QUIC or Quick UDP Internet Connections is built on UDP and focuses on improved internet performans and security.

ARP or Address Resolution Protocol is used to map an IP address to a MAC address on a local network.

#### T1-2

IPV4: 177
IPV6: 1

DNS SERVER IP: 172.25.8.8

Ipv4 is the global standard for websites and ipv6 is not as commonly used.

The DNS server is used to translate the specified domain name to an IP address.

#### T1-3

The protocals that are used are DNS and QUIC

DNS is used to translate domain names to IP addresses.

QUIC is built on UDP and focuses on improved internet performans and security.

TCP is used to ensure accurate data transfer between devices over a network.

### Task 2

#### T2-1

Ip my machine:
172.27.149.173

Ip for other servers:
20.42.73.27
52.56.120.249
172.25.8.8
128.119.245.12
52.3.167.79

HTTP request message:

GET /wireshark-labs/HTTP-wireshark-file1.html HTTP/1.1

Using the method GET on the URL /wireshark-labs/HTTP-wireshark-file1.html with HTTP/1.1

#### T2-2

HTTP Respond message:

|Status code |Content length|modified last time|
|-|-|-|
|200 OK|540|wed, 20 Nov 2024 14:48:47 GMT|

HTTP/1.1 200 OK (text/html)

Status codes are used to indicate the result of a servers attempt to complete the request. Content length indicates on how many bytes the responds are. Modified last time indicates when the respons was last modified.

### Task 3

#### T3-1

First GET on /wireshark-labs/HTTP-wireshark-file2.html with http/1.1 includes the headers Accept, upgrade-Insecure-Recuests, User-Agent, Accept-Encoding, Accept-Language, Connection and Host.

The response is Status code 200 OK, Content length 784 and Last Modified Sun, 01 Dec 2024 06:59:01 GMT, Date Sun, 01 Dec 2024 14:02:28 GMT.

On relode of the site, GET on /wireshark-labs/HTTP-wireshark-file2.html with http/1.1 includes the headers Accept, upgrade-Insecure-Recuests, User-Agent, Accept-Encoding, Accept-Language, Connection and Host.

The response is Status code 200 OK, Content length 784 and Last Modified Sun, 01 Dec 2024 06:59:01 GMT, Date Sun, 01 Dec 2024 14:02:39 GMT.

### Task 4

#### T4-1

There is only one recuset sent from the user to the server and in the response there are 4 reassembled TCP segments wwith the length of 1460, 1460, 1460 and 471 for a total of 4861 bytes. TCP have a maximum of 1500 bytes in size, where 20 bytes is the minimum header size and 20 bytes is for the IP address. Hence 1500 - 20 - 20 = 1460 which is the maximum size of the segment.

#### T4-2

Http uses TCP as its underlying transportation layer protocal to transfer long files. The connection is initilied by a http recuest for the file. Then using TCP a three way handshake is established, then the file size is sent in the content length. The data is then sent over using TCP segments untill the content length is reached. The segment size ca vary depending on the what is mutually agreed upon in the three way handshake. The data is then reassembled by using the sequence number assigned to the segments. Errors in the data is checked when recived by the client using the checksums that are generated by the TCP for each segment.

#### T4-3

Status codes are 3 digit numbers that indicates the outome of the request.

1xx - information, recived, processes continuing
2xx - Successfully recevied, understood or accepted
3xx - Redirection, need furder acction
4xx - Client error, can not be fulfiled
5xx - Server error, failed to fulfill recuest

The http reason phrase is a short text phrase that explains the status code. For example 404 Not Found where the first part is the status code and the second part is Not Found.

### Task5

#### T5-1

GET recuese on /wireshark-labs/protected_pages/HTTP-wireshark-files5.html with HTTP/1.1 without credentials.

The response is 401 unauthorized

The header www-Autenticate using Basic authentication using the realm "wireshark-students only".

When the username and password is inputed there is a new header thats Authorization with Basic authentication and the Credentials as the username and the password.

The response has the status code of 200 OK that confirmes the credentials being correct.

The problems with the password protection is that its using Basic Authentication which uses Base64-encoded plaintext. Base64-encoding is not a secure way to encode the credentials.
