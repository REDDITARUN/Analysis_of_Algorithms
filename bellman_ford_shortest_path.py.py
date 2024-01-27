#First take all..vokey
n_vertexo, m_edgeoo = map(int, input().split())
graph_edg = []

for go in range(m_edgeoo):
    firstnide, secnod, w = map(int, input().split())
    graph_edg.append((firstnide, secnod, w))
#nEXT FORD ALFO
def BELLAM(n_vertexo, graph_edg):

    #initializeoo
    dist_till_now = [float('inf')] * (n_vertexo + 1)
    dist_till_now[1] = 0


    for _ in range(n_vertexo - 1):
        for u, v, w in graph_edg:
            if dist_till_now[u] != float('inf') and dist_till_now[u]+ w <dist_till_now[v]:
                dist_till_now[v] = dist_till_now[u]+ w


    if dist_till_now[n_vertexo]!=float('inf'):
        return dist_till_now[n_vertexo]
    
    else: 
        return "INFINITY"


res = BELLAM(n_vertexo, graph_edg)
print(res)


#Reference - Lecure Slides