
import heapq

# implement the FF (Farthest-In-Future) 
def ffuture(cachesize, reqlist):
    ffstoredch = []  # storecache
    countmiss = 0  # count the number os misses
    future_page_indices = []

    #Go yjrough the each request
    for page in reqlist:
        if page not in ffstoredch:  # Check if the page is not stored cache then 
            countmiss =countmiss+ 1  # add 1 to the miss count also add the page
            ffstoredch.append(page)  

            if len(ffstoredch) > cachesize:
                # Use a min-heap to find the farthest future page to replace
                future_page_indices = []
                for i, x in enumerate(ffstoredch):
                    if x in reqlist[i+1:]:
                        future_page_indices.append((reqlist[i+1:].index(x), x))
                if future_page_indices:
                    farthest_future_page = min(future_page_indices, key=lambda pair: pair[0])[1]
                    ffstoredch.remove(farthest_future_page)
    return countmiss

# implement the FIFO (First-In-First-Out) 
def fifo_algorithm(cachesize, reqlist):
    fifostc = []  
    countmiss = 0  

    for page in reqlist:
        if page not in fifostc:  
            countmiss += 1  
            fifostc.append(page) 

            if len(fifostc) > cachesize:
                fifostc.pop(0)  
    return countmiss




# Take inpuuts
cachesize=0
nopg=0
nopgreq=0
reqlist = []

cachesize, nopg, nopgreq = map(int, input().split())

for _ in range(nopgreq):
    temp = int(input())
    reqlist.append(temp)


ffmisses = ffuture(cachesize, reqlist)
# print(ffmisses)
fifomisses = fifo_algorithm(cachesize, reqlist)
# print(fifomisses)

diff = fifomisses-ffmisses
print(diff)
