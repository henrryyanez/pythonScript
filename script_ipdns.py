import tkinter as tk
import socket
import re
import urllib

nombre_equipo = socket.gethostname()
direccion_equipo = socket.gethostbyname(nombre_equipo)
dato=urllib.request.urlopen("http://checkip.dyndns.org").read()
dato1=str(dato)
m = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', dato1)
m2=m[0]

print("El nombre de tu equipo es: " + nombre_equipo)
print("La IP privada es: "+direccion_equipo)
print("La IP pública es: "+m2)
