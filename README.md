# NetworkMap

README 

Network Map Visualization Script

*Description*

This Python script, networkmap.py, visualizes a local network by pinging IP addresses in a specified subnet and plotting the responsive hosts in a 3D graph using the matplotlib and networkx libraries.

*Features*

 - Ping Hosts: Uses ARP and ICMP to check for active devices in the specified subnet.
 - 3D Network Visualization: Creates a three-dimensional network graph where each node represents a device on the network.
 - Response Time Mapping: The nodes are plotted with a z-coordinate proportional to the ping response time, providing a visual representation of network latency.

*Requirements*

 - Python 3.x
 - Networkx
 - Matplotlib
 - Numpy
 - Scapy

*Installation*

To run this script, ensure you have all the required libraries installed. You can install them using pip:

 > bash pip install networkx matplotlib numpy scapy

*Usage*

Specify Subnet: The script is set to scan the IP addresses from 192.168.1.1 to 192.168.1.254 by default.

Run Script: Execute the script using Python:

 > bash python networkmap.py

View Visualization: A 3D plot will be displayed with your device at the center and other network devices surrounding it, plotted based on their response times.

*Code Overview*

ping(ip): Function that sends ARP and ICMP requests to a given IP address. It returns the response time if the host responds, otherwise it returns None.

create_3d_network(subnet): Main function that generates the network graph. It iterates over IP addresses, pings them, and adds responding hosts as nodes in a 3D network graph.

Visual Output: The script uses matplotlib's 3D plotting capabilities to display the nodes and edges, coloring each node to differentiate your computer from other network devices.

**Disclaimer*

This program is to be used strictly for Educational Purposes with the goal of demonstrating Network Topology and Analysis. 

License
This project is licensed under the MIT License - see the LICENSE file for details.
