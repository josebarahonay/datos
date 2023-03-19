# c = open('chanchito.txt', 'a')

# c.write('\nagregaremos una nueva linea a nuestro archivo')

# c.close()

# x = open('chanchito.txt')

# print(x.read())

# x.close()

import os

# eliminar un archivo
if os.path.exists('chanchito.txt'):
    os.remove('chanchito.txt')
else:
    print('El archivo no existe')

# eliminar un directorio
#os.rmdir('micarpeta')

print("otra modificacion")