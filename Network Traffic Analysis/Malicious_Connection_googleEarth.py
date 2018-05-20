# -*- coding: utf-8 -*-
"""
@author: scrutineermonk
"""

import dpkt
import socket
import geoip2.database
reader = geoip2.database.Reader('FULL PATH\GeoLite2-City_20180501\GeoLite2-City.mmdb')  ## Give full path of geo databse,
## get the databse from https://dev.maxmind.com/geoip/geoip2/geolite2/

##### Creates the KML file for IP
def retKML(ip):
    ipInfo=reader.city(ip)
    try:
        longitude=ipInfo.location.longitude
        latitude=ipInfo.location.latitude
        
############### KML File For Globe Icon   --- Not using here; uncomment if want to use instead of simple placemaker
        
#        kml=('<Placemark>\n'
#             '<name>%s</name>\n'
#             '<visibility>0</visibility>\n'
#             '<LookAt>\n'
#             '<longitude>%.6f</longitude>\n'
#             '<latitude>%.6f</latitude>n'
#             '<altitude>0</altitude>\n'
#             '<heading>-148.4126684946234</heading>\n'
#             '<tilt>40.55750733918048</tilt>\n'
#             '<range>365.2646606980322</range>\n'
#             '</LookAt>\n'
#             '<styleUrl>#globeIcon</styleUrl>\n'
#             '<Point>\n'
#             '<extrude>1</extrude>\n'
#             '<altitudeMode>relativeToGround</altitudeMode>\n'
#             '<coordinates>%.6f,%.6f</coordinates>\n'
#             '</Point>\n'
#             '</Placemark>\n'
#             )%(ip,longitude,latitude,longitude,latitude)


############### KML File For Simple Icon   --- Using simple one here.
        kml=('<Placemark>\n'
             '<name>%s</name>\n'
             '<Point>\n'
             '<coordinates>%.6f,%.6f</coordinates>\n'
             '</Point>\n'
             '</Placemark>\n'
             )%(ip,longitude,latitude)
        return kml
    except Exception as e:
        return ''
        


##### Creates KML File for all the IP's found in pcap File

def plotIPs(pcap):
    KMLPts=''
    kmldoc=''
    IPAssociated=[]
    for (ts,buf) in pcap:
        try:
            eth=dpkt.ethernet.Ethernet(buf)
            ip=eth.data
            src = socket.inet_ntoa(ip.src)
            if src not in IPAssociated:
                IPAssociated.append(src)
                srckml=retKML(src)
                KMLPts=KMLPts+srckml
            dst = socket.inet_ntoa(ip.dst)
            if dst not in IPAssociated:
                IPAssociated.append(dst)
                dstkml=retKML(dst)
                KMLPts=KMLPts+dstkml
            print("IPAssociated: "+IPAssociated)
        except:
            pass
        kmlheader=('<?xml version="1.0" encoding="UTF-8"?>\n'
                   '<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n')
        kmlfooter='</Document>\n</kml>\n'
        kmldoc=kmlheader+KMLPts+kmlfooter
    print(IPAssociated)
    return kmldoc
            

def main():
    file='FULL PATH OF PCAP File/geofinal.pcap'  ## Give full path of pcap capture
    f=open(file, 'rb')
    kmlfile=open("kmldoc.kml",mode="w+")  ## Creates new file named kmldoc.kml in working directory
    pcap=dpkt.pcap.Reader(f)
    kmldoc=plotIPs(pcap)
    kmlfile.write(kmldoc)
    kmlfile.close()
    print("Success")
    
if __name__=='__main__':
    main()
