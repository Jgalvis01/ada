"""
Julian Andres Galvis
29/03/2025
The Settlers of Catan
"""
from sys import stdin
 
def catan(node, nodes, count):
    global flags
    global solvs
    solvs = max(solvs, count)
    for i in nodes[node]:
        edge = (min(node, i), max(node, i))
        if not flags.get(edge, False):
            flags[edge] = True
            catan(i, nodes, count + 1)
            flags[edge] = False

def main():
    global flags
    global solvs

    line = list(map(int, stdin.readline().strip().split()))
    while line[0] != 0 and line[1] != 0:
        n = line[0]
        m = line[1]
        solvs = 0
        nodes = [[] for _ in range(n)]
        for _ in range(m):
            a, b = map(int, stdin.readline().strip().split())
            nodes[a].append(b)
            nodes[b].append(a)
        
        flags = {}
        
        for i in range(n):
            catan(i, nodes, 0)
        
        print(solvs)
        
        line = list(map(int, stdin.readline().strip().split()))
        
main()