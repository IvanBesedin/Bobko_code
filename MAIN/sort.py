def sort(message):
    data = dict()
    for letter in message:
        if letter not in data:
            data[letter] = 1
        else:
            data[letter] += 1

    return data
