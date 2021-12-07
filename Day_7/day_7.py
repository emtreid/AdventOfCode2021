def checkFuelCost(data, position):
    costs = [abs(x-position) for x in data]
    return sum(costs)

def checkFuelCostNonLinear(data, position):
    distance = [abs(x-position) for x in data]
    costs = [x*(x+1)/2 for x in distance]
    return int(sum(costs))

def findMinCost(checkFuelCost, sortedData):
    positions = [x for x in range(sortedData[0], sortedData[-1])]
    fuelCosts = [checkFuelCost(sortedData, x) for x in positions]
    return min(fuelCosts)

if __name__ == "__main__":

    with open("input.txt") as f:
        data = [int(x) for x in f.read().strip().split(",")]

    data.sort()

    print("PART 1:")
    print(findMinCost(checkFuelCost, data))

    print("PART 2:")
    print(findMinCost(checkFuelCostNonLinear, data))