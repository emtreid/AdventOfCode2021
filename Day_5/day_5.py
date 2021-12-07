with open('input.txt') as f:
    data = [x.split(" -> ") for x in f.read().splitlines()]

start = [x[0] for x in data]
end = [x[1] for x in data]

start_points = [[int(x.split(",")[0]),int(x.split(",")[1])] for x in start]
end_points = [[int(x.split(",")[0]),int(x.split(",")[1])] for x in end]

seafloor_one = [[0]*1000 for i in range(1000)]
seafloor_two = [[0]*1000 for i in range(1000)]

def addline(seafloor, start, end):
    if start[0] == end[0]:
        for j in range(min(start[1], end[1]), max(start[1], end[1])+1):
            seafloor[j][start[0]] += 1
    elif start[1] == end[1]:
        for i in range(min(start[0], end[0]), max(start[0], end[0])+1):
            seafloor[start[1]][i] += 1
    return seafloor

def addline_with_diagonal(seafloor, start, end):
    if start[0] == end[0]:
        for j in range(min(start[1], end[1]), max(start[1], end[1])+1):
            seafloor[j][start[0]] += 1
    elif start[1] == end[1]:
        for i in range(min(start[0], end[0]), max(start[0], end[0])+1):
            seafloor[start[1]][i] += 1
    else:
        distance = abs(end[0]-start[0])+1
        x_sign = (end[0]-start[0])/abs(end[0]-start[0])
        y_sign = (end[1]-start[1])/abs(end[1]-start[1])
        for i in range(distance):
            seafloor[int(start[1]+i*y_sign)][int(start[0]+i*x_sign)] += 1
    return seafloor

def iterate(function, seafloor, start_points, end_points):
    for i in range(len(start_points)):
        seafloor = function(seafloor, start_points[i], end_points[i])
    return seafloor

seafloor_one = iterate(addline, seafloor_one, start_points, end_points)
seafloor_two = iterate(addline_with_diagonal, seafloor_two, start_points, end_points)

print("PART 1: ")
print([len([x for l in seafloor_one for x in l if x>1])])

print("PART 2: ")
print([len([x for l in seafloor_two for x in l if x>1])])
