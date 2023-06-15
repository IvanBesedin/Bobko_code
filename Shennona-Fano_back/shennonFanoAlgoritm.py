class Compressed():

    def __init__(self, code, dictionary):
        self.code = code
        self.dictionary = dictionary
        self.values = list(dictionary.values())
        self.keys = list(dictionary.keys())


def compute_half_pos(list_to_divide):
    local_sum = 0
    half_sum = float(sum(list_to_divide) / 2)

    for element in (range(len(list_to_divide))):
        local_sum += list_to_divide[element]
        if local_sum + list_to_divide[element + 1] >= half_sum:
            delta_i = abs(local_sum - half_sum)
            delta_i_plus_1 = abs(local_sum + list_to_divide[element + 1] - half_sum)
            if delta_i < delta_i_plus_1:
                # print(element)
                return element
            # print(element)
            return element + 1


def shennon_fano_iteration(dictionary, prev_iteration=""):
    match len(dictionary):
        case 0:
            return {}
        case 1:
            if prev_iteration == "":
                return {list(dictionary.keys())[0]: "0"}
            return {list(dictionary.keys())[0]: prev_iteration}

    n = compute_half_pos(list(dictionary.values()))
    # print(n)
    new_part0 = dict(((list(dictionary.items()))[0:n + 1]))
    new_part0 = shennon_fano_iteration(new_part0, prev_iteration + "0")

    new_part1 = dict(((list(dictionary.items()))[n + 1:]))
    new_part1 = shennon_fano_iteration(new_part1, prev_iteration + "1")

    new_part0.update(new_part1)
    return new_part0
