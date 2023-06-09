from max_value import lengths, mayor, max_value
def shennon_fano_decompression(code, dict_binary_to_letters):
    """Decompresses a string code of 0 -s and 1 -s, using a dictionary, and returns a letter string.

    Takes as a parameter a string code of 0 -s and 1 -s, and a dictionary that has a structure {Binary code : Letter}
    """

    code_complexity = ()

    max = max_value(dict_binary_to_letters)

    message = ""
    symbol = ""

    for n in code:
        symbol += n
        attempt = dict_binary_to_letters.get(symbol, False)

        if attempt:
            message += attempt
            symbol = ""

        if len(symbol) > max:
            return "Обнаружена ошибка"

    return message
