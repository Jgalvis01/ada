"""
Julian Andres Galvis
18/02/2025
Hashing map
"""

from sys import stdin

def hash_map(L,S,i):

    ans = 0
    if i > 26:
        ans = 0
    elif (L != 0 and S == 0) or (L == 0 and S != 0):
        ans = 0
    elif S == 0 and L == 0:
        ans = 1
    else:
        ans = ans + hash_map(L,S,i+1)
        if i <= S:
            ans = ans + hash_map(L-1,S-i,i+1)
    return ans

def solve(L,S):

    ans = 0
    s1 = S - (S//L)
    l_copy = L 
    s_copy = S
    i=1
    ans = hash_map(l_copy,s_copy,i)
    
    return ans

def main():

    L,S = map(int,stdin.readline().strip().split())
    while L != 0 and S != 0:
        print(solve(L,S))
        L,S = map(int,stdin.readline().strip().split())
    
main()


