

import heapq

def partition(intervalslist):
    intervalslist.sort(key=lambda x: x[1])
    machines = [] 
    num_machines = 0

    for everyinterval in intervalslist:
        start, end = everyinterval
        if not machines or machines[0] > start:
            num_machines += 1
            heapq.heappush(machines, end)
        else:
            heapq.heappop(machines)  
            heapq.heappush(machines, end)

    return num_machines


intervalnumber = int(input())
intervalslist = []
for eachinterval in range(intervalnumber):
    stime, etime = map(int, input().split())
    intervalslist.append((stime, etime))

machines = partition(intervalslist)
print(machines)

