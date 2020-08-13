import re

mensaje = 'Buscando numero telefonico 33-445566 oculto en 33-445-566 el text'

#Aplico expresion regular en texto sin quitar grupo
phoneNumRegex = re.compile(r'\d{2}-\d{6}')
mo = phoneNumRegex.search(mensaje)
print(mo.group())

#Separo por grupos:
phoneNumRegex = re.compile(r'(\d{2})-(\d{3})-(\d{3})')
mo = phoneNumRegex.search(mensaje)
print(mo.group(3))

#Patrones o grupos opcionales:
phoneNumRegex = re.compile(r'(\d{2}-)?(\d{3}-\d{3})')
mo = phoneNumRegex.search(mensaje)
print(mo.group())
