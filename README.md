 
 # Violent_Python_Projects
The repository contains python codes written while studying the Violent Python Book. 


 # KML_File_Output.py
 Gives KML file as an output. Scenario: While investigating an infected machine, we came across with IP to which infected machine connected. We specified the IP addresses and got KML as output. Once KML is uploaded to google earth, we were able to see the places where the connection was made, helping in the better understanding of attack locations.
 
 # Malicious_Connection_googleEarth.py
 The objective is same as KML_File_Output.py but rather than specifying each and every IP manually, the code takes PCAP capture of infected machine as an input and gives an output of a KML file. Once KML is uploaded to google earth, we were able to see the places where the connection was made, helping in the better understanding of attack locations and correlating the locations.
 
 # VulnerabilityScanner101.py
 The objective of the script is to connect to IP/Network and scan for the host which might be vulnerable. Script take in a text file as a command line argument. This text file should have a list of banners associated with vulnerable services. 
 Scenario: Script can be used where we need to check quickly our network on ADHOC basis for some services.
 
 # getLocation.py
 The script gives location details as output for the IP specified.
 
 # readPcapFiles.py
 The script takes a pcap file as an input and provides the connection directions as an output. 
 Scenario: Script can be used to analyze quickly all the connections made by infected machines.
