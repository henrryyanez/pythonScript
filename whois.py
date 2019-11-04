import whois
import datetime
import csv

def test_whois():
    dnsFile = open('dominios.txt', 'r')
    for line in dnsFile:
        lookup = line.rstrip()
        w = whois.whois(lookup)
        print(w.creation_date, line)
    dnsFile.close()

out = test_whois()

#with open("resultado" + ".txt","w") as h:
#    h.write(str.test_whois())
#    h.close()
