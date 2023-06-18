from shennonFanoCompression import shennon_fano_compression


def lengths(message):
    result = shennon_fano_compression(message)
    x = result.dictionary
    lengths = []  # List to save lenghts

    for key in x:
        length = len(key)  # Find the key lenght
        lengths.append(length)  # Add the lenght to the list
    return lengths


def max_value(dict_binary_to_letters):
    max = 0

    for i in list(dict_binary_to_letters.keys()):

        if len(i) > max:
            max = len(i)

    return max


def mayor(lista):  # Determine max value
    max = lista[0]
    for x in lista:
        if x > max:
            max = x
    return max
