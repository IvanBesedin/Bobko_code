from shennonFanoCompression import shennon_fano_compression
def lengths(message):
    result = shennon_fano_compression(message)
    x = result.dictionary
    lengths = []  # List to save lenghts

    for key in x:
        length = len(key)  # Find the key lenght
        lengths.append(length)  # Add the lenght to the list
    return lengths




def mayor(lista): # Determine max value
    max=lista[0]
    for x in lista:
        if x > max:
            max = x
    return max

