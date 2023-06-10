def read(path = "data_set\\message.txt"):
    str = ""
    with open(path, encoding="UTF-8") as file:
        for line in file:
            str += line
    return str