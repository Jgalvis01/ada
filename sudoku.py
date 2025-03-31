"""
Julian Andres Galvis
28/03/2025
So Doku Checker
"""
from sys import stdin


answers = 0

def check(r, c, p, T):
    ans = True
    i = 0
    aux = T[r][c] 
    T[r][c] = 0
    if answers == 2:
        ans = False
    else:
        while i < 9 and ans:
            if T[i][c] == p or T[r][i] == p:
                ans = False
            i += 1
        rr, cc = (r // 3) * 3, (c // 3) * 3
        i = rr
        while i < rr + 3 and ans:
            j = cc
            while j < cc + 3 and ans:
                if T[i][j] == p:
                    ans = False
                j += 1
            i += 1
        T[r][c] = aux
    return ans

def forwardCheck(T):
    ans = True
    i = 0
    while i < 9 and ans:
        j = 0
        while j < 9 and ans:
            if T[i][j] == 0:
                aux = T[i][j]
                T[i][j] = 0
                candidate_found = False
                num = 1
                while num < 10 and not candidate_found:
                    if check(i, j, num, T):
                        candidate_found = True
                    num += 1
                ans = candidate_found
                T[i][j] = aux
            j += 1
        i += 1
    return ans

def getCell(T):
    
    min = 10
    best = None
    flag = True
    i = 0
    while i < 9 and flag:
        j = 0
        while j < 9 and flag:
            if T[i][j] == 0:
                count = 0
                for v in range(1, 10):
                    if check(i, j, v, T):
                        count += 1
                if count < min:
                    min = count
                    best = (i, j)
                    if min == 1:
                        flag = False
            j += 1
        i += 1
    return best

def backSudoku(r, c, T ,flag):
    
    global answers 
    if answers < 2:        
        k = 0
        while k < 9 and flag:
            j = 0
            while j < 9 and flag:
                if T[k][j] != 0:
                    flag = check(k, j, T[k][j], T)    
                j += 1
            k += 1
        if flag:          
            cell = getCell(T)
            if cell is None:
                answers += 1
            else:
                r, c = cell
                for i in range(1, 10):
                    if check(r, c, i, T):
                        T[r][c] = i
                        if forwardCheck(T):
                            next = getCell(T)
                            if next is None:
                                answers += 1
                            else:
                                rr, cc = next
                                backSudoku(rr, cc, T, True)
                        T[r][c] = 0
        else:
            answers = 3
        
def main():
    
    global answers
    lines = [line.strip() for line in stdin if line.strip()]
    grids = []
    for i in range(0, len(lines), 9):
        grid = []
        for j in range(i, i + 9):
            row = list(map(int, lines[j].split()))
            grid.append(row)
        grids.append(grid)
    
    i = 1
    for grid in grids:
        next = getCell(grid)
        if next is None:
            answers = 1
        else:
            r, c = next
            backSudoku(r, c, grid, True)
        if answers == 0:
            print(f"Case {i}: Impossible.")
        elif answers == 1:
            print(f"Case {i}: Unique.")
        elif answers == 2:
            print(f"Case {i}: Ambiguous.")
        else:
            print(f"Case {i}: Illegal.")
        answers = 0
        i += 1
        
                  
main()