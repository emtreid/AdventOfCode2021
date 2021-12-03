from os import error
from typing import List

def invert(x: str):
    if x == "1":
        return "0"
    elif x == "0":
        return "1"
    else:
        raise ValueError("Argument should be \"1\" or \"0\"")

def concat_column(binary_list: List[str], i: int) -> str:
    return "".join([x[i] for x in data])

def most_common(bit_string:str):
    n_one = bit_string.count("1")
    n_zero = bit_string.count("0")
    return "1" if n_one>n_zero else "0"

def bit_filter(binary_list: List[str], i: int, most: bool) -> str:
    if len(binary_list) == 1:
                return binary_list[0]

    bit_string = "".join([x[i] for x in binary_list])
    n_one = bit_string.count("1")
    n_zero = bit_string.count("0")

    if (n_zero>n_one) ^ most :
        reduced_list = [x for x in binary_list if x[i]=="1"]
    else:
        reduced_list = [x for x in binary_list if x[i]=="0"]
    
    return bit_filter(reduced_list, i+1, most)


with open('input.txt') as f:
    data = f.read().splitlines()

bit_columns = [concat_column(data, i) for i in range(len(data[0]))]

gamma_string = "".join([most_common(x) for x in bit_columns])
epsilon_string = "".join([invert(most_common(x)) for x in bit_columns])

gamma = int(gamma_string, 2)
epsilon = int(epsilon_string, 2)

print("PART 1:")
print(gamma*epsilon)

oxygen_string = bit_filter(data, 0, True)
carbon_string = bit_filter(data, 0, False)

oxygen = int(oxygen_string, 2)
carbon = int(carbon_string, 2)

print("PART 2:")
print(oxygen*carbon)
