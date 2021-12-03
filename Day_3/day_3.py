from typing import List

with open('input.txt') as f:
    data = f.read().splitlines()

def bit_filter(binary_list: List[str], i: int, most: bool):
    if len(binary_list) == 1:
            return binary_list

    bit_string = "".join([x[i] for x in binary_list])
    n_one = bit_string.count("1")
    n_zero = bit_string.count("0")
    
    if (n_zero>n_one) ^ most :
        return [x for x in binary_list if x[i]=="1"]
    else:
        return [x for x in binary_list if x[i]=="0"]

gamma = ""
epsilon = ""

for i in range(len(data[0])):

    bit_string = "".join([x[i] for x in data])
    n_one = bit_string.count("1")
    n_zero = bit_string.count("0")
    
    if n_zero>n_one:
        gamma += "0"
        epsilon += "1"
    else:
        epsilon += "0"
        gamma += "1"

print("PART 1:")
print(int(gamma, 2)*int(epsilon,2))

oxygen_list = data
carbon_list = data

for i in range(len(data[0])):
    oxygen_list = bit_filter(oxygen_list, i, True)
    carbon_list = bit_filter(carbon_list, i, False)

print("PART 2:")
print(int(oxygen_list[0], 2)*int(carbon_list[0],2))
