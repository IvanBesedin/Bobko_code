from shennonFanoCompression import shennon_fano_compression
from text_read import read

result = shennon_fano_compression()
x = result.dictionary
lengths = []  # Lista para almacenar las longitudes

for key in x:
    length = len(key)  # Calcular la longitud de la clave
    lengths.append(length)  # Agrega la longitud a la lista




def mayor(lista): # Definir el valor maximo.
    max=lista[0];
    for x in lista:
        if x > max:
            max = x
    return max
print(read())
print(result.dictionary)
print("Longitudes:", lengths)  # Imprime la lista de longitudes
print("самый длинный-это", mayor(lengths))






