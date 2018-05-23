# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:56:09 2018

@author: scrutineermonk
"""
from scapy.all import *

file='FUllpath/domainFlux.pcap' ## Specify the full path of the pcap capture of Conficker worm

def dnsQRTest(pkt):  ### take a single packet as input and return TRUE is query is unanswered.
    if pkt.haslayer(DNSRR) and pkt.getlayer(UDP).sport == 53:   ### checkes only reply from DNS Server
        rcode=pkt.getlayer(DNS).rcode  ### Every dns reply will have a rcode, if rcode == 3 means dns query failed, if 0 success
        qname=str(pkt.getlayer(DNSQR).qname) ### Name of query
        qname=qname.replace("b'","") ### Remove some strings
        if rcode == 3:
            print("[!] Name request Lookup Failed: "+str(qname))
            return True
        else:
            return False

def main():
    unAnsReq=0
    pkts=rdpcap(file)  ### Read pcap file
    for pkt in pkts:  ### iterate over each packet
        if dnsQRTest(pkt):
            unAnsReq=unAnsReq+1
    print('[!]'+str(unAnsReq)+' Unanswered Name Request')  ### Finally prints no. of dns query failed
    
if __name__ == '__main__':
    main()
