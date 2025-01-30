from scapy.all import ARP, Ether, srp
import argparse
import re
from prettytable import PrettyTable
from mac_vendor_lookup import MacLookup, VendorNotFoundError

def arp_scan(target_ip):
    # Create an ARP request packet to send to the network
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # Send the packet and capture the response
    result = srp(packet, timeout=3, verbose=0)[0]

    # Print out the MAC, IP addresses, and vendors of all devices that responded
    table = PrettyTable(["IP", "MAC", "Vendor"])
    for sent, received in result:
        mac = received.hwsrc
        ip = received.psrc
        try:
            vendor = MacLookup().lookup(mac)
        except VendorNotFoundError:
            vendor = "Unknown"
        table.add_row([ip, mac, vendor])
    print(table)

if __name__ == "__main__":
    # Use argparse to parse the target IP range from the command line
    parser = argparse.ArgumentParser(description="Perform an ARP scan on a target IP range.")
    parser.add_argument("target_ip", help="The target IP range to scan (e.g., 192.168.1.1/254)")
    args = parser.parse_args()

    # Run the ARP scan and print the results
    arp_scan(args.target_ip)
