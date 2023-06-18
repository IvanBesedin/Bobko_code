from shennonFanoAlgoritm import shennon_fano_iteration, Compressed
from text_read import read
from sort import sort


def shennon_fano_compression(message = ""):
    """Compress a string to a binary code.

    Gets a string from message.txt file and returns a Compressed object.
    Compressed obj contains code and dictionary. Code is a string of binary, and dictionary is a dict BinaryToSymbol.
    {Binary code : Symbol}
    """
    if message == "":
        message = read()
    dictionary = sort(message)

    sorted_data = dict(reversed(sorted(dictionary.items(), key=lambda item: item[1])))

    dict_letters_to_binary = shennon_fano_iteration(sorted_data)

    dict_binary_to_letters = {}

    for key, value in dict_letters_to_binary.items():
        dict_binary_to_letters[value] = key

    generated_code = ""

    for letter in message:
        generated_code += dict_letters_to_binary[letter]

    result = Compressed(generated_code, dict_binary_to_letters)

    return result
