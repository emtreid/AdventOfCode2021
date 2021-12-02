with open('input.txt') as f:
    data = [int(x) for x in f.read().splitlines()]

diff = [data[i+1]-data[i] for i in range(len(data)-1)]

positive_diff = [i for i in diff if i>0]

print("PART 1:")
print(len(positive_diff))

average_diff = [data[i+3]-data[i] for i in range(len(data)-3)]

positive_average_diff = [i for i in average_diff if i>0]

print("PART 2:")
print(len(positive_average_diff))