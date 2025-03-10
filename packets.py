"""
Julian Andres Galvis
08/03/2025
Packets
"""

from sys import stdin

def packets(line,i):
    ans = None
    if i == len(line):
        ans = 0
    elif line[i] == 0:
        ans = packets(line,i+1)
    else:
        if i == 1:
            aux = 11 * line[i]
            line[len(line)-1] = max(0,line[len(line)-1] - aux)
            ans = line[i] + packets(line,i+1)
        elif i == 2:
            aux = 5 * line[i]
            if aux - line[len(line)-2] > 0:
                aux = aux * 4
                line[len(line)-1] = max(0,line[len(line)-1] - aux)
            line[len(line)-2] = max(0,line[len(line)-2] - aux)
            ans = line[i] + packets(line,i+1)
        elif i == 3:
            aux = line[i] // 4
            aux2 = line[i] % 4
            if aux2 > 0:
                aux = aux + 1
                if aux2 == 1:
                    line[len(line)-2] = max(0,line[len(line)-2] - 5)
                    line[len(line)-1] = max(0,line[len(line)-1] - 7)
                elif aux2 == 2:
                    line[len(line)-2] = max(0,line[len(line)-2] - 3)
                    line[len(line)-1] = max(0,line[len(line)-1] - 6)
                elif aux2 == 3:
                    line[len(line)-2] = max(0,line[len(line)-2] - 1)
                    line[len(line)-1] = max(0,line[len(line)-1] - 5)
                
            ans = aux + packets(line,i+1)
        elif i == 4:  
            aux = line[i] // 9
            aux2 = line[i] % 9
            if aux2 > 0:
                aux = aux + 1
                line[len(line)-1] = max(0,line[len(line)-1] - (36 - aux2*4))
            ans = aux + packets(line,i+1)
        elif i == 5:
            aux = line[i] // 36
            aux2 = line[i] % 36
            if aux2 > 0:
                aux = aux + 1
            ans = aux + packets(line,i+1)

    return ans 

def main():
    
    line = list(map(int, stdin.readline().strip().split()))
    p1 = line[0]
    p2 = line[1]
    p3 = line[2]
    p4 = line[3]
    p5 = line[4]
    p6 = line[5]
    
    while not (p1 == 0 and p2 == 0 and p3 == 0 and p4 == 0 and p5 == 0 and p6 == 0):
        
        line.reverse()
        print( line[0] + packets(line,1))
        
        line = list(map(int, stdin.readline().strip().split()))
        p1 = line[0]
        p2 = line[1]
        p3 = line[2]
        p4 = line[3]
        p5 = line[4]
        p6 = line[5]

main()