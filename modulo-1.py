import modules as xs
from camelcase import CamelCase

print(xs.mascotas)

xs.saludo('Nicolas')

c = CamelCase()
s = 'esta oracion necesita CamelCase!'

camelcased = c.hump(s)
print(camelcased)
#print(mascotas)
#saludo('Nicolas')


