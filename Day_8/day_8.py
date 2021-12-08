def identify(digits):
    remaining_digits = ["a", "b", "c", "d", "e", "f", "g"]
    all_segments = "".join(digits)
    mapping = {}
    ones = [x for x in digits if len(x)==2][0]
    sevens = [x for x in digits if len(x)==3][0]
    fours = [x for x in digits if len(x)==4][0]
    mapping["F"] = [x for x in ones if all_segments.count(x)==9][0]
    remaining_digits.remove(mapping["F"])
    mapping["C"] = [x for x in ones if all_segments.count(x)==8][0]
    remaining_digits.remove(mapping["C"])
    mapping["A"] = sevens.replace(mapping["F"], "").replace(mapping["C"], "")
    remaining_digits.remove(mapping["A"])
    mapping["B"] = [x for x in fours if x in remaining_digits and all_segments.count(x)==6][0]
    remaining_digits.remove(mapping["B"])
    mapping["D"] = [x for x in fours if x in remaining_digits and all_segments.count(x)==7][0]
    remaining_digits.remove(mapping["D"])
    mapping["E"] = [x for x in remaining_digits if all_segments.count(x)==4][0]
    remaining_digits.remove(mapping["E"])
    mapping["G"] = remaining_digits[0]
    return mapping

def map_segments(mapping, digit):
    for key in mapping.keys():
        digit = digit.replace(mapping[key], key)
    return digit

def decode(mapping, number):
    true_digits = ["ABCEFG", "CF", "ACDEG", "ACDFG", "BCDF", "ABDFG", "ABDEFG", "ACF", "ABCDEFG", "ABCDFG"]
    mapped_number = [map_segments(mapping, x) for x in number]
    sorted_number = ["".join(sorted(x)) for x in mapped_number]
    int_number = int("".join([str(true_digits.index(x)) for x in sorted_number]))
    return int_number

if __name__ == "__main__":

    with open('input.txt') as f:
        data = [x.split(" | ") for x in f.read().splitlines()]

    digits_list = [x[0].split(" ") for x in data]
    numbers = [x[1].split(" ") for x in data]

    unique_lengths = [2, 3, 4, 7]

    print("PART 1:")
    print(len([x for l in numbers for x in l if len(x) in unique_lengths]))

    maps = [identify(digits) for digits in digits_list]

    print("PART 2:")
    print(sum([decode(maps[i], numbers[i]) for i in range(len(numbers))]))