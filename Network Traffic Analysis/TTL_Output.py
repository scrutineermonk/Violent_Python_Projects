from scapy.all import *
#from IPy import IP as IPTEST
import ipaddress


def testTTL(pkt):  ### Takes a single packet as input
    try:
        if pkt.haslayer(IP):   ## checkes if packet has IP layer in it
            ipsrc=pkt.getlayer(IP).src ### fetchs the IP header then gives src IP address from IP header
            ip=ipaddress.ip_address(ipsrc)
            print("IP address: "+str(ipsrc))
            if ip.is_private:
                return
            else:
                ttl=pkt.getlayer(IP).ttl  ### fetchs the IP header then gives src IP address from IP header
                print('[+] Packet received from: '+str(ipsrc)+' with TTL: '+str(ttl))
    except Exception as e:
        pass

def main():
#    sniff(prn=lambda x: x.show())  ## sniffs all the network adaptors, we can specify adaptor also. prn is a syntax used to perform
                                     ## some action on every packet captured. We can use lambda if only 1 action is required on packet
    sniff(prn=testTTL, store=0, count=100)
if __name__ == '__main__':
    main()
