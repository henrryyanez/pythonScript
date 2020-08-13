import re

mensaje = 'Buscando numero telefonico 33-445566 oculto en el text'
phoneNumRegex = re.compile(r'\d{2}-\d{6}')
mo = phoneNumRegex.search(mensaje)
print(mo.group())
