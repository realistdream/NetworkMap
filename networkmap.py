import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scapy.all import sr, srp, IP, ICMP, ARP, Ether

def ping(ip):
    """Returns response time if host responds to a ping, None otherwise."""
    arp_req = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    answered, _ = srp(arp_req, timeout=1, verbose=0)

    if not answered:
        return None

    packet = IP(dst=ip)/ICMP()
    answered, _ = sr(packet, timeout=1, verbose=0)

    if not answered:
        return None

    sent_time, received = answered[0]
    response_time = received.time - sent_time.time
    return response_time

def create_3d_network(subnet):
    G = nx.Graph()

    central_node = "My Computer"
    G.add_node(central_node, color='b', position=(0.5, 0.5, 0.5))

    for i in range(1, 255):  
        ip = f"{subnet}.{i}"
        response_time = ping(ip)

        if response_time is not None:
            print(f"Received response from {ip} in {response_time:.4f} seconds")
            z_position = 0.5 + response_time  
            G.add_node(ip, color='g', position=(np.random.rand(), np.random.rand(), z_position))
            G.add_edge(central_node, ip, weight=response_time)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for node, data in G.nodes(data=True):
        x, y, z = data['position']
        ax.scatter(x, y, z, c=data['color'])
        if data['color'] == 'g':
            ax.text(x, y, z, node, size=10, zorder=1, color='k')  

    for u, v in G.edges():
        x0, y0, z0 = G.nodes[u]['position']
        x1, y1, z1 = G.nodes[v]['position']
        ax.plot([x0, x1], [y0, y1], [z0, z1], c='grey')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()

if __name__ == '__main__':
    create_3d_network('192.168.1')

