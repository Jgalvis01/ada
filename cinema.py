"""
Julian Andres Galvis
26/04/2025
Cinema-cola
"""
import sys

def main():
    stdin = sys.stdin
    R, C = map(int, stdin.readline().split())
    while R != 0 and C != 0:
        matriz = [[True] * (C+1) for _ in range(R)]
        P = int(stdin.readline().strip())
        for _ in range(P):
            sit, signo = stdin.readline().split()
            r = ord(sit[0]) - ord('A')
            c = int(sit[1:]) - 1
            s = c if signo == '-' else c+1
            matriz[r][s] = False

        Z = int(stdin.readline().strip())
        friends = []
        for _ in range(Z):
            sit = stdin.readline().strip()
            r = ord(sit[0]) - ord('A')
            c = int(sit[1:]) - 1
            friends.append((r, c))

        friends.sort(key=lambda x: (x[0], x[1]))
        
        flag = True
        i = 0

        while i < len(friends) and flag:
            if not matriz[friends[i][0]][friends[i][1]]:
                if matriz[friends[i][0]][friends[i][1] + 1]:
                    matriz[friends[i][0]][friends[i][1] + 1] = False
                else:
                    flag = False
            i += 1
        
        if flag:
            print("YES")
        else:
            print("NO")
            
        R, C = map(int, stdin.readline().split())

main()