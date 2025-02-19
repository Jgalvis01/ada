"""
Julian Andres Galvis
18/02/2025
Hashing map
"""

from sys import stdin

def hash_map(L,S,i,mem):
    
    if (L,S,i) in mem: ans = mem[(L,S,i)]
    else:
        ans = 0
        if i > 27:
            ans = 0
        elif S < L:
            ans = 0
        elif (L != 0 and S == 0) or (L == 0 and S != 0):
            ans = 0
        elif S == 0 and L == 0:
            ans = 1
        else:
            if i <= S:
                ans = ans + hash_map(L-1,S-i,i+1,mem)
            ans = ans + hash_map(L,S,i+1,mem)
        mem[(L,S,i)] = ans
    return ans

def solve(L,S):

    ans = 0
    i=1
    
    max = sum(range(26 - L + 1,27))
    if S > max:
        ans = 0
    elif L > 26:
        ans = 0
    elif S > 351:
        ans = 0
    elif S < L:
        ans = 0
    else:
        mem = {}
        ans = hash_map(L,S,i, mem)
    return ans

def main():

    L,S = map(int,stdin.readline().strip().split())
    p = 1
    while L != 0 and S != 0:
        print("Case {}: {}".format(p,solve(L,S)))
        p += 1
        L,S = map(int,stdin.readline().strip().split())
    
main()

