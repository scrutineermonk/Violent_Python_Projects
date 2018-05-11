# -*- coding: utf-8 -*-
"""
@author: scrutineermonk
"""

# Code reads the pcap files and prints connections as output.

import dpkt
import socket
def printPcap(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print('Source: ' +src+ ' -----> Destination: '  +dst)
        except:
            return


def main():
    file='FULL PATH/geotest.pcap' ## Specify the full path of pcap file
    f=open(file, 'rb')
    pcap=dpkt.pcap.Reader(f)
    printPcap(pcap)
    

if __name__ == '__main__':
    main()
