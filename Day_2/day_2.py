with open('input.txt') as f:
    data = f.read().splitlines()

direction = [x.split(" ")[0] for x in data]
distance = [int(x.split(" ")[1]) for x in data]

up = sum([distance[i] for i in range(len(distance)) if direction[i] == "up"])
down = sum([distance[i] for i in range(len(distance)) if direction[i] == "down"])
forward = sum([distance[i] for i in range(len(distance)) if direction[i] == "forward"])

depth = down-up

print("PART 1:")
print(depth*forward)

def findaim(direction, distance, i):
    up = sum([distance[i] for i in range(i) if direction[i] == "up"])
    down = sum([distance[i] for i in range(i) if direction[i] == "down"])
    return down-up

aim = [findaim(direction,distance, i) for i in range(len(distance))]

forward = sum([distance[i] for i in range(len(distance)) if direction[i] == "forward"])
depth = sum([distance[i]*aim[i] for i in range(len(distance)) if direction[i] == "forward"])

print("PART 2:")
print(depth*forward)