# -*- coding: utf-8 -*-
"""
@author: scrutineermonk
"""

import geoip2.database
reader = geoip2.database.Reader('FULL PATH\GeoLite2-City_20180501\GeoLite2-City.mmdb')


def printRecord(tgt):
    
    try:
        response=reader.city(tgt)
        country_name=response.country.name
        cn_name=response.country.names['zh-CN']
        iso_code=response.country.iso_code
        sub_division=response.subdivisions.most_specific.name
        subdivision_iso_code=response.subdivisions.most_specific.iso_code
        city_name=response.city.name
        postal_code=response.postal.code
        time_zone=response.location.time_zone
        long=response.location.longitude
        lat=response.location.latitude
        print("[*]Target "+tgt+" Geo-Located")
        print("[+]Country: "+ country_name + " -- "+cn_name+" -- ISO-Code: "+iso_code)
        print("[+]Subdivision: "+ sub_division + " -- ISO-Code: "+subdivision_iso_code)
        print("[+]City: "+city_name+" -- Postal Code: "+postal_code)
        print("[+]TimeZone: "+time_zone)
        print("[+]Maxmind: "+maxmind)
        print("[+]Latitude: "+str(lat)+", "+"Longitude: "+str(long))
        print(country_name+'-'+city_name)
        return
    
    except:
        print("Address not Found")
        return


def main():
    print("Welcome to Target Geo-Locater")
    tgt=input("Enter the Target IP address to be Located: ")
    print("Geo Locating Target: "+tgt)
    printRecord(tgt)



if __name__ == '__main__':
    main()
