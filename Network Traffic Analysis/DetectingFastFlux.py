# -*- coding: utf-8 -*-
"""
Created on Sun May 20 23:47:35 2018

@author: scrutineermonk
"""

from os import *

from scapy.all import *
dnsRecords={}
file='FUllpath/domainFlux.pcap' ## Specify the full path of the pcap captur


### Handle Packet
def handlePkt(pkt):
#    qname=pkt.getlayer(DNSQR).qname
    if pkt.haslayer(DNSRR):  ## Checks if packet if dns reply
        rrname=str(pkt.getlayer(DNSRR).rrname) ## get the query name
        rrname=rrname.replace("b'","")
#        print("Response"+str(pkt.getlayer(DNSRR).rrname))
#        print(str(pkt.getlayer(DNS).rcode))
#        print("Query"+str(pkt.getlayer(DNSQR).qname))
#        print(str(pkt.getlayer(DNSRR).rdata))
#        print(str(pkt.getlayer(DNSRR)))
        rrname=rrname.replace("'","")
        rdata=pkt.getlayer(DNSRR).rdata  ### gets the response IP
        if rrname in dnsRecords:  ## Checks if query already in main dictionary 
            if rdata in dnsRecords[rrname]: ### Checks if IP already received for that query
                return
            else:
                dnsRecords[rrname].append(rdata) ### If IP in new for the query, adds the IP to list, list if value of query as key in global dictionary
                return
        else:
            dnsRecords[rrname]=[]  ### If query is observed for the 1st time creats a new key value pair in dictionary, value as empty list
            dnsRecords[rrname].append(rdata) ### append the data to the empty list
            return dnsRecords


def main():
    pkts=rdpcap(file)
    for pkt in pkts:
        handlePkt(pkt)
    for item in dnsRecords:
        print('[+] '+item+' has '+str(len(dnsRecords[item])))
            
if __name__ == '__main__':
    main()
