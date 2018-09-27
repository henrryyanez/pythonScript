#script para traer ip addresses de repetidores tor utilizando la libreria stem

from stem.descriptor.remote import DescriptorDownloader
import re
cont = 0
infoCompleta = ""
downloader = DescriptorDownloader()
for descriptor in downloader.get_consensus().run():
  if descriptor.exit_policy.is_exiting_allowed():
    ipFind = re.findall( r'[0-9]+(?:\.[0-9]+){3}', str(descriptor))
    ipFind.pop(1)
    
    infoCompleta = infoCompleta + "\n" + str(ipFind)
    cont = cont + 1
print (r"+------------------------------+")
print (r"|     IP DE LOS NODOS          |")
print (r"+------------------------------+")
print (infoCompleta)

print (r"+-------------------------+")
print (r"| CONTEO DE NODOS ACTIVOS |")
print (r"+-------------------------+")
print ("Existen: " + str(cont) + " nodos tor")
print (r"+-------------------------+")
