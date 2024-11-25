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
    - QUIC
        
        A transport layer protocol designed by Google that aims to reduce latency and improve connection speeds, using UDP instead of TCP.

    - DNS
        
        A system that translates human-readable domain names like "www.example.com" into IP addresses.

## Problem 2 

- T2-1 
    - My computers IP: `172.27.140.238`

    - Other IPs:

        - `172.25.8.8` 
    
        - `142.250.74.100`
    
        - `128.119.245.12`

    - Observation of request:
        
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

## Problem 4 : TODO : Data exists 

- T4-1 

There is only one request packet sent to the server. The packet length encompasses the size of the file that is requested by the client.

![T4](./img/T4-1.png)

- T4-2 



- T4-3 



## Problem 5 : TODO : Data exists

- T5-1 

