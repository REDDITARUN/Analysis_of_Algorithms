
def isbip(G, root):
    nodesvisited = set()  # This stores the nodes visited with their colors
    colourstore = {}  # Dictionary to store the colors
    colourstore[root] = 0  # The initial color will be zero

    Q = []
    Q.append(root)

    while Q:
        vertexu = Q.pop(0)

        if vertexu not in nodesvisited:
            nodesvisited.add(vertexu)

            for vertexv in G.get(vertexu, []):  # Fixed the variable name vertexv
                if vertexv not in colourstore:
                    colourstore[vertexv] = 1 - colourstore[vertexu]  # Give the opposite color
                    Q.append(vertexv)
                elif colourstore[vertexv] == colourstore[vertexu]:
                    return False
    return True

G = {}
nov, noe = map(int, input().split())
for i in range(noe):
    vertexu, vertexv = map(int, input().split())
    if vertexu not in G:
        G[vertexu] = []
    if vertexv not in G:
        G[vertexv] = []
    G[vertexu].append(vertexv)
    G[vertexv].append(vertexu)

bipartitegrapho = isbip(G, list(G.keys())[0])

if bipartitegrapho:
    print("yes")
else:
    print("no")
