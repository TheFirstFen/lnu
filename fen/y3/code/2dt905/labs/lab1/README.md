# 2DT905 : Lab 1 : [Samuel Berg](mailto:sb224sc@student.lnu.se)

## Problem 1

- T1-1 
    - ARP (Address Resolution Protocol)
        
        A protocol used to map a network address like an IP address to a physical address (MAC address) on a local network.

    - DNS (Domain Name System)
        
        A system that translates human-readable domain names like "www.example.com" into IP addresses.

    - TCP (Transmission Control Protocol)
        
        A connection-oriented protocol that ensures reliable data transmission by establishing a connection and performing error checking.

    - TLSv1.2 / TLSv1.3 (Transport Layer Security)
        
        Protocols that provide secure communication over a computer network by encrypting data. TLSv1.3 is the more recent and secure version compared to TLSv1.2.

    - ICMP (Internet Control Message Protocol)
        
        A network layer protocol used for diagnostic and error reporting, such as pinging to test connectivity.

    - QUIC (Quick UDP Internet Connections)
        
        A transport layer protocol designed by Google that aims to reduce latency and improve connection speeds, using UDP instead of TCP.

    - UDP (User Datagram Protocol)
        
        A connectionless protocol that sends data without establishing a reliable connection, often used for streaming or real-time communications.

    - WLCCP (Wireless LAN Context Control Protocol)
        
        A protocol used in wireless networks to manage the context information of mobile clients, primarily in Cisco wireless systems.

- T1-2 
    - IPv4 conversations: 81

    - IPv6 conversations: 1 

    - DNS Server IP: `172.25.8.8` (Which I assume to be the router due to it having the websites that I visited cached)

    - IPv4 vs. IPv6

        There is a significant difference in the number of IPv4 and IPv6 conversations because IPv4 remains the dominant protocol in most networks, with wider use and compatibility. IPv6 is used less frequently due to limited use and is typically only utilized when explicitly required.

    - DNS Server

        The DNS server used in this capture is `172.25.8.8` which is likely the router acting as the DNS server. It caches frequently accessed domain names, providing faster responses and reducing the need for external DNS queries.

- T1-3 
    - UDP (User Datagram Protocol)
        
        A connectionless protocol that sends data without establishing a reliable connection, often used for streaming or real-time communications.
    - QUIC
        
        A transport layer protocol designed by Google that aims to reduce latency and improve connection speeds, using UDP instead of TCP.
    - DNS
        
        A system that translates human-readable domain names like "www.example.com" into IP addresses.
    - ICMP (Internet Control Message Protocol)
        
        A network layer protocol used for diagnostic and error reporting, such as pinging to test connectivity.

## Problem 2 

- T2-1 
    1. My computers IP: `172.27.140.238`

    2. Other IPs:
        * IP: `172.25.8.8` 
    
        * IP: `142.250.74.100`
    
        * IP: `128.119.245.12`

    3. Observation of request:
        
        Using `GET` on URI `/wireshark-labs/HTTP-wireshark-file1.html` and specifying request version as `HTTP/1.1`. 

- T2-2 
    - Status Code: `200 (OK)`
        
        Refers to the request being accepted and going through.

    - Content Length: `128`
        
        Refers to the size of the response.

    - Last-Modified: `Wed, 20 Nov 2024 06:59:01 GMT`
        
        Refers to the last time the file was modified.

## Problem 3 

- T3-1 
    - Observations:

        First `GET` request on URI `/wireshark-labs/HTTP-wireshark-file2.html` specifying version as `HTTP/1.1`. Includes the following headers: `Host`, `Connection`, `DNT`, `Upgrade-Insecure-Requests`, `User-Agent`, `Accept`, `Accept-Encoding` and `Accept-Language`. 

        First response: Status Code: `200 (OK)`, Content Length: `371`, Last-Modified: `Wed, 20 Nov 2024 06:59:01 GMT`.

        Second `GET` request on URI `/wireshark-labs/HTTP-wireshark-file2.html` specifying version as `HTTP/1.1`. Includes the same headers as the first `GET` request and the following new ones: `Cache-Control`, `If-None-Match` and `If-Modified-Since`.

        Second response: Status Code: `304 (Not Modified)`.

    - Explanation of second request and response:

        The three new headers in the `GET` request which assists in validation that the resource has not been changed since last visit and the server can then avoid a redundant data transfer by confirming the resource has gone unmodified. Hence the response `Status Code: 304 (Not Modified)`.

## Problem 4 

- T4-1 

There is only one request packet sent to the server when doing it on Linux and the response is all in the HTTP response. On Windows there is one request packet but there are 3 response TCP packets with data and the remaining data is sent in the HTTP response. 

TCP has a minimum header size of 20 bytes, the IP header size is 20 bytes and the maximum segment size for a TCP segment is 1500 bytes (which is negotiated at the handshake interaction). By doing simple math we can conclude that the data size for each TCP segment should max out at $1500 - 20 - 20 = 1460 bytes$ which you can see in the capture on my Windows machine. Also according to this the fact that I am getting all the data in the HTTP response points to that my Linux machine negotiated a larger maximum segment size during the handshake.  

![T4-linux](./img/T4-1-linux.png)
*Note: When doing the capture on my Linux machine.*

![T4-win](./img/T4-1-win.png)
*Note: When doing the capture on my Windows machine.*

- T4-2 

HTTP relies on TCP for the data transmission. When a client requests a large file over HTTP it is transferred as a stream of data managed by the TCP protocol. A connection is initialized by a HTTP request for a file then a TCP connection is established by a three-way handshake. The entire file size is sent in the `Content-Length` header and the data is streamed over TCP segments till it reaches the size specified in the `Content-Length`. The data is sent in TCP segments over the network. The segment sizes can vary depending on the type of network and what is mutually agreed upon in the handshake when establishing the connection. Segment reassembly is done by looking up the sequence numbers assigned to each segment by the TCP and assembling them in order of the sequence numbers. Errors in the data are detected with the help of checksums that are generated by the TCP on each segment which is then checked upon reaching the client. 

- T4-3 

1. **Status Code**
    * **1xx (Informational)**: Request received. Processing continues.
    * **2xx (Success)**: Request successfully processed.
    * **3xx (Redirection)**: Further action required to complete the request.
    * **4xx (Client Error)**: Problem with the request.
    * **5xx (Server Error)**: Server failed to fulfill a valid request.
2. **Reason Phrase**

Human readable explanation of status code. Useful for debugging or to display for end-user.


## Problem 5 

- T5-1 

1. First `GET` request and response
    * Requests a password-protected resource `HTTP-wireshark-file5.html`.
    * Server responds with `401 Unauthorized` which indicates that the client did not include valid credentials in the request.
    * The header `WWW-Authenticate` in the response specifies `Basic` authentication with a realm `"wireshark-students only"` prompting the client to provide credentials.
2. Second `GET` request and response 
    * Client resends the request with the `Authorization` header including the login and password. They are `Base64-encoded` to the following string `d2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms=` which is decoded to `wireshark-students:network`
    * Server responds with `200 OK` confirming the credentials being correct and authentication going through and providing the requested resource.
3. Problems
    * The `Basic` authentication transmits the credentials as Base64-encoded plaintext which is a secure as storing the user details in pure plaintext. The "best" and "simplest" solution to this type of problem would be to implement everything the same but instead of using HTTP protocol using HTTPS which would solve the encryption and plaintext data issues.
