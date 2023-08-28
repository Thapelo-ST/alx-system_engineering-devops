## Web infrastructure
In this project we focused more on what is a web infrastructure, its mainly the underlying technology and architecture that supports the functioning of a website

It has all kinds of components that support a web based application or website like firewalls, DNS's, servers and more, and it also insclude other hardware, network, server and software components.

A breif insight about the components:
- Server: is a computer of software system that provides services or resources to the other compute clients over network, but mostly internet, they can store data, host websites and more.
- Domain Name: human-readable address that is used to identify and access resources on the internet, such as websites.
-  Application Server: handles the dynamic processing of requests by running server-side scripts or applications. Those processes may be interacting with databases, generate customized content etc.
-  Web Server:  receives and processes incoming HTTP requests from clients, retrieve the requested web content (such as HTML, images, etc.) from its storage, and send it back as HTTP responses to the clients.
-  Database: stores and manages structured data used by the application. It can be used to store user information, content, settings, and more. They are a very efficient way to store, retrieve, update, and manipulate data.
-  Firewall: helps control incoming and outgoing traffic, while HTTPS ensures encrypted communication between users and the server.
-  Monitoring tools: provide insights into the health and performance of the infrastructure.

## 0-simple_web_stack
In the picture provided you can see that the simple infrastructure consists of one of every components. and they have been explained what they are in the begining of the document.

How it works:
- the client inserts foobar.com or www.foobar.com and sends the HTTPS request over the browser
- the browser connects to the internet and checks if the domain name is configured in the DNS
- then it continues to the server of the requested website
- the sever has a component that wasnt explained before of which is the codebase,
- Code Base is the complete body of source code for a software program, component or system.

What can be the issue about this infrastructure?
- SPOF (Single Point Of Failure): with this infrastructure if the server goes down the entire infrastructure unavaliable rendering everything useless.
- Downtime During Maintenance: if and when the update towards the website is implemented users may maynot be able to access the application or website because of having one server, thus it cant rotate between servers for accesibility.
- Cannot scale for high traffic: the rapid increase volume of traffic could crash the server, appliction server, and database. 

## 1-distributed_web_infrastructure
In this task the added components: is an additional server, and one load-balancer.
This infrastucture works similar to the first one just added more componets and some of the processes changed a bit. But the primary ones remained the same.

Reasons for adding componets:
- adding an additional server eleminates the SPOF that was present in the first infrastructure
- Load-balancer to discribute incoming traffic across multiple servers, improving performance, availability, and ensuring that no single server becomes overwhelmed.
- adding another database replicating the primary database cluster, to enhance database reliability by setting up replication. The primary node handles write operations, while the replica nodes help distribute read requests and act as failover in case the primary node fails.

Nodes:
- Primary Node: Handles write operations (inserts, updates, deletes) and ensures data consistency. It's responsible for maintaining the authoritative copy of the data.
- Replica Node: Replicates data from the Primary and serves read requests. It acts as a backup and can be promoted to the Primary role in case of a failure.

Some issues with this infrastructure:
- SPOF if the balancer can become unvaliable.
- Lack of firewalls, this can lead to security vulnerabilities 
- No monitoring: without any monitoring tool or tools, the issue of addressing security breaches, performance issues, or othe operational problems may become difficult.

## 2-secured_and_monitored_web_infrastructure
In this task, I added:
one more server, making it 3 servers, 1 SSL certificate, and 3 monitoring clients and firewalls.

Reasons for adding componets:
- the other server increases the avalibility of the website, or application and decreases the rates of crashing and failure.
- adding firewalls helps to regulate and filter incoming and outgoing traffic, preventing unauthorized access and potential attacks from malicious entities.
- SLL Certificate: because this infrastructure serves on HTTPS, that encrypts data durung transmission. it ensures a secure connection between users and servers.
- monitoring clients, help track the infrastructure's performance, resource usage, and security metrics. This aids in identifying bottlenecks, anomalies, and security breaches.

Issues that can be encounted with this infrastructure:
- Terminating SSL at the load balancer means that the encrypted traffic is decrypted there, potentially exposing sensitive data before it reaches the application server, thus posing a security risk.
- Relying on a single MySQL server for write operations can lead to a SPOF, if the server fail, write operations will be disrupted after affecting data consistency and avaliability.
- Having identical components on all servers can lead to resource imbalances. For instance, if a server is heavily loaded due to high web traffic, it could also experience strain on the application server and database, leading to performance issues.
