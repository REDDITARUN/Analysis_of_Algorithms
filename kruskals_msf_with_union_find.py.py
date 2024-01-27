class disjoint:
    def __init__(self, n):
        self.prev = [i for i in range(n)]
        self.node_set = [0] * n

    def find(self, u):
        if u != self.prev[u]:
            self.prev[u] = self.find(self.prev[u])
        return self.prev[u]

    def union(self, u, v):
        u_node, v_node = self.find(u), self.find(v)
        if u_node == v_node:
            return False
        if self.node_set[u_node] < self.node_set[v_node]:
            self.prev[u_node] = v_node
        elif self.node_set[u_node] > self.node_set[v_node]:
            self.prev[v_node] = u_node
        else:
            self.prev[v_node] = u_node
            self.node_set[u_node] += 1
        return True


# # FIrst take all the inputs
n_vertex, m_edge, k = map(int, input().split())
edges_graph = [] #initialozo
for edges in range (m_edge):
    u, v, weighto = map(int, input().split())
    edges_graph.append((u,v,weighto))



#let's solce using krushkal
def msf(n_vertex, edges_graph, k):
    #were suing disjoing here
    disj = disjoint(n_vertex)
    edges_graph.sort(key=lambda x: x[2])
    #nect initialize
    count_of_tree = n_vertex
    count_of_forest = 0
    

    for node1, node2, weights in edges_graph:
        if disj.union(node1-1, node2-1):
            count_of_forest = count_of_forest + weights
            count_of_tree = count_of_tree - 1
            if count_of_tree==k:
                break

    return count_of_forest
   

min_sp_tree = msf(n_vertex, edges_graph, k)
print(min_sp_tree)


# https://plainenglish.io/blog/union-find-data-structure-in-python-8e55369e2a4f
