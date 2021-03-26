def truckTour(petrolpumps):
    #
    # Write your code here.
    #
    start = 0
    current = 0
    tank = 0
    while start < len(petrolpumps):
        tank += petrolpumps[current][0]
        tank -= petrolpumps[current][1]
        current = (current+1) % len(petrolpumps)
        if tank < 0:
            start = current
            tank = 0
        else:
            if current == start:
                return start