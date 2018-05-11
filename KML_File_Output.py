# -*- coding: utf-8 -*-
"""
@author: scrutineermonk
"""

import geoip2.database
## Download the geo databse 
reader = geoip2.database.Reader('FULL PATH\GeoLite2-City.mmdb') ## reads the databse


def retKML(ip):
    ipInfo=reader.city(ip)
    try:
        longitude=ipInfo.location.longitude
        latitude=ipInfo.location.latitude
        kml=('<Placemark>\n'
             '<name>%s</name>\n'
             '<Point>\n'
             '<coordinates>%.6f,%.6f</coordinates>\n'
             '</Point>\n'
             '</Placemark>\n'
             )%(ip,longitude,latitude)
        return kml
    except Exception as e:
        input("Error")
        return ''

kmlPts=''   
ip1='208.73.210.87'  ## specify the IP address for which KML file is to be generated
ip1K=retKML(ip1)
ip2='208.73.23.67'
ip2K=retKML(ip2)
kmlPts=kmlPts+ip1K+ip2K ## prepares the body of the KML file
## KML header
kmlheader=('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n')
## KML Footer
kmlfooter='</Document>\n</kml>\n'
kmldoc=kmlheader+kmlPts+kmlfooter
print(kmldoc)  ## Full KML file as Output
