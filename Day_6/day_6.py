with open('input.txt') as f:
    data = [int(x) for x in f.read().split(",")]

fish_numbers = [data.count(i) for i in range(9)]

print(fish_numbers)

def spawn(fish_numbers):
    new_numbers = [fish_numbers[i+1] for i in range(8)]
    new_numbers[6] += fish_numbers[0]
    new_numbers.append(fish_numbers[0])
    return new_numbers

def loop_spawn(fish_numbers, n):
    for i in range(n):
        fish_numbers = spawn(fish_numbers)
    return(fish_numbers)

print("PART 1:")
print(sum(loop_spawn(fish_numbers, 80)))

print("PART 2:")
print(sum(loop_spawn(fish_numbers, 256)))