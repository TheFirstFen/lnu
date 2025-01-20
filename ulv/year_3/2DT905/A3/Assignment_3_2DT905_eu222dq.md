# Assignment 3 2DT905

## Emil Ulvagården (<eu222dq@student.lnu.se>)

### Task 1

#### A Base system

![base](T1a-base.png)

#### B Ping between pc

![pc1](T1b-pc1.png)

![router1](T1b-router1.png)

Due to a lack of configuration between hosts. Packages can only be sent direct to other hosts.

#### C Network module

NM-1FE-TX: Network Module single Fast Ethernet port transmit interface. Used to add an additional ethernet port to a router.

NM-16ESW: Network Module 16 Ethernet Switch. Used to act as a small ethernet switch in a router.

WIC-1T: Wide Area Network Interface Card 1 serial port. Used to connect routers in serial link.

NM-16ESW is not a good alternativ due to that NM-16ESW does not have the necessary routing capabilities as its a primary use is for switching.

#### D Subnet

A /24 subnet has 254 usable addresses. 256 total, 1 for the network and 1 for broadcast. Sutiable for local area networks with multiple devices.

A /30 subnet has 2 usable addresses. 4 total, 1 for the network and 1 for broadcast. Sutiable for point to point network.

### Task 2

#### A ip route

ip route [ip] [mask] [router_interface] [metric]

[ip] The target network for the static route

[mask] The subnet mask for the destination network

[router_interface] The address for the next router

[metric] The cost of the route

#### B Traceroute pc

![t2b](T2b-pc1.png)

The path is R1 -> R4 -> R5 due to how the metric is used. Where the bandwidth 100Mbps gives a 1 as metric, 10 Mbps gives 2 av metric and 1544kbps gives a 3. R1 first chooses one of the two available routers with 1 as metric and then follows that path which in this case is the path through R4.

![T2b](T2b-pc3.png)

The path is R5 -> R3 -> R2 -> R1 due to how the metrics are used. R5 first chooses the path with the lowest metric which is the path through r3 and r2 to R1.

#### C Path shutdown

![pc1cont](T2c-pc1cont.png)

![pc3cont](T2c-pc3cont.png)

#### D Path shutdown, new path

![tracepc1-pc3](T2d-Tracepc1-pc3.png)

The packages starts taking the route R1 -> R4 -> R5. When that route is shutdown four packages are lost untill the new route R1 -> R2 -> R3 -> R5 is found. This new route is choosen as the metric for the path is the new lowest.

![tracepc3-pc2](T2d-Tracepc3-pc2.png)

The packages starts taking the route R5 -> R3 -> R2 -> R1. When the route is shutdown two packages are lost untill the new route R5 -> R1 is found. This new route is choosen as the metric for the path is the lowest.

### Task 3

#### A RIP path

![pc1RIP](T3a-pc1RIP.png)

RIP selects the best path depending on the amount of routers the packages needs to pass through to get to the destination. The path R1 -> R5 is the best as it has 1 hop while the path R1 -> R4 -> R5 has 2 hops and the path R1 -> R2 -> R3 -> R5 has 3 hops.

![pc3RIP](T3a-pc3RIP.png)

The path R5 -> R1 is the best as it has 1 hop while the path R5 -> R4 -> R1 has 2 hops and the path R5 -> R3 -> R2 -> R1 has 3 hops.

#### B RIP new path

![pc1-RIP-shut](T3b-pc1-RIP-shut.png)

When the path R1 -> R5 is shutdown the new path is the path with the lowest amounts of hops which is the path R1 -> R4 -> R5.

![pc3-RIP-shut](T3b-pc3-RIP-shut.png)

When the path R5 -> R1 is shutdown the new path is the path with the lowest amounts of hops which is the path R5 -> R4 -> R1.

### Task 4

#### A OSPF metric

OSPF uses cost as a metric. The cost is calculated as cost = (Refernece Bandwidth) / (Link Bandwidth)

The default Reference Bandwidth is 100Mbps. The lowest cost is the path R1 <-> R2 <-> R3 <-> R5, and the highest cost is the path R1 <-> R4 <-> R5.

The path R1 <-> R5 has the cost 10. The path R1 <-> R2 <-> R3 <-> R5 has the cost of 3. The path R1 <-> R4 <-> R5 has and approximate cost of 66.

#### B OSPF new path

![pc1-ospf](T4a-pc1-ospf.png)

The lowest cost is first the path R1 -> R2 -> R3 -> R5 and when that path is shutdown the new lowest costing path is R1 -> R5 which is why that path is now choosen.

![pc3-ospf](T4a-pc3-ospf.png)

The lowest cost is first the path R5 -> R3 -> R2 -> R1 and when that path is shutdown the new lowest costing path is R5 -> R1 which is why that path is now choosen.

### Task 5

TODO: summary

Static routing simple for small networks but complex for larger networks due to manuall updates for possible changes in the metrics. Static routing is effitent due to defiend routes. Fast recovery if other routes are available, in task 2D the amount of packages that are lost are 4 and 2, which is an low amount.

RIPv2 relatively simple for small to medium sized networks. Low efficiency due to hop based metric that ignores the bandwidth and speed of the link. Slow recovery if other routes are available, in task 3B the amount of packages that are lost are 8 and 18 which is a high amount compared to static routing and OSPF.

OSPF is more complex but sutiable for medium to large networks. Very effitent due to the use of metrics based on the bandwidth that a link provides. Relativly fast recovery when other routes are available, in task 4B the amount of packages that are lost are 5 and 5, which is relativly low.
