"""
Julian Andres Galvis
27/04/2025
Numerical Maze
"""
max_sequence = []
start = (0,0)
end = (0,0)

from sys import stdin

def check(maze , i, j, q):
    global max_sequence
    ans = []
    if q + 1 < len(max_sequence):
        
        serch = max_sequence[q + 1]
        r = len(maze)
        c = len(maze[0])
        if 0 <= i + 1 < r and 0 <= j + 0 < c:
            if maze[i + 1][j] == serch:
                ans.append((i + 1, j))
        if 0 <= i - 1 < r and 0 <= j + 0 < c:
            if maze[i - 1][j] == serch:
                ans.append((i - 1, j))
        if 0 <= i + 0 < r and 0 <= j + 1 < c:
            if maze[i][j + 1] == serch:
                ans.append((i, j + 1))
        if 0 <= i + 0 < r and 0 <= j - 1 < c:
            if maze[i][j - 1] == serch:
                ans.append((i, j - 1))
    return ans
    
def maze_find(maze,q, i, j, path):
    global start, end, max_sequence
    if i == len(maze) - 1:
        if end == None or j < end[1]:
            end = (i, j) 
    else:
        if maze[i][j] == max_sequence[q]:
            going = check(maze, i, j, q)
            going.sort(key=lambda x: x[1])
            for ni, nj in going:
                if (ni, nj) not in path:
                    path.append((ni, nj))
                    maze_find(maze, q + 1, ni, nj, path)
                    path.pop()
            
def main():
    cases = int(stdin.readline().strip())
    for z in range(cases):
        global start, end
        blank = stdin.readline().strip()
        R, C = map(int, stdin.readline().split())
        maze = [[0] * C for _ in range(R)]
        max = 0
        for _ in range(R):
            numeros = list(map(int, stdin.readline().strip().split()))
            for j in range(C):
                maze[_][j] = numeros[j]
                if numeros[j] > max:
                    max = numeros[j]

        global max_sequence
        for k in range(1, max+C):
            max_sequence.extend(range(1, k+1))
            
        path = []
        c = 0
        start = None
        end = None
        while c < C and end == None:
            if maze[0][c] == max_sequence[0]:
                start = (0, c)
                path.append((0, c))
                maze_find(maze, 0, 0, c, path)
                path.pop()
            c += 1
        print(f"{start[0]+1} {start[1]+1}")
        print(f"{end  [0]+1} {end  [1]+1}")
        if z != cases - 1:
            print()
main()