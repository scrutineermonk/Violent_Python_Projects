# -*- coding: utf-8 -*-
"""
Created on Sun May 20 16:45:41 2018

@author: scrutineermonk
"""

from scapy.all import *
#from IPy import IP as IPTEST
import ipaddress
import time
IP_TTL={}
thresh=5

## Takes src_ip and it's TTl value and gives output if IP is spoofed

def checkTTL(src_ip, ttl):
#    print(str(type(ttl))) ### src_ip is a string; ttl in int
    if src_ip in IP_TTL:
        return
    print('------------------Checking Whether Spoofed or Not-----------------------')
    pkt=sr1(IP(dst=src_ip) / ICMP(), \
            retry=0, timeout=1, verbose=0)
    IP_TTL[src_ip]=pkt.ttl ## pkt.ttl is int 
#    print(str(IP_TTL))
    print('TTL Received: '+str(ttl))
    print('TTL Calculated: '+str(IP_TTL[src_ip]))
    if abs(int(pkt.ttl)-int(ttl)) > thresh:
        print("[+]Detected Possible Spoofed Packet From: "+str(src_ip))
        print("[!] Spoofed TTL: "+str(ttl)+" Actual TTL: "+str(IP_TTL[src_ip])+'\n\n')
    else:
        print("Probably True IP\n\n")



## Takes packet and extracts TTL values from non-private IP's

def testTTL(pkt):  ### Takes a single packet as input
    try:
        if pkt.haslayer(IP):   ## checkes if packet has IP layer in it
            ipsrc=pkt.getlayer(IP).src ### fetchs the IP header then gives src IP address from IP header
            ip=ipaddress.ip_address(ipsrc)
#            print("_______________________________________________________NEW CONNECTION________________________________________________")
#            print("Connection from IP address: "+str(ipsrc))
            if ip.is_private:  ## discards private IP Range
                return
            elif ipsrc in IP_TTL:
                return
            ttl=pkt.getlayer(IP).ttl  ### fetchs the IP header then gives src IP address from IP header
            print('[+] Packet received from: '+str(ipsrc)+' with TTL: '+str(ttl))
            checkTTL(ipsrc,ttl)
                
                
    except Exception as e:
#        print("Error: "+ str(e))
        pass




def main():
#    sniff(prn=lambda x: x.show())  ## sniffs all the network adaptors, we can specify adaptor also. prn is a syntax used to perform
                                     ## some action on every packet captured. We can use lambda if only 1 action is required on packet
    sniff(prn=testTTL, store=0, count=1000)
    print(str(IP_TTL))
    
    
if __name__ == '__main__':
    main()
