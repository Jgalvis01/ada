"""
Julian Andres Galvis
09/03/2025
Keep the Customer Satisfied
"""

from sys import stdin
import heapq

def customer(orders):
    
    ans = []
    acum = 0
    for i in range(len(orders)):
        heapq.heappush(ans, -orders[i][0])
        acum += orders[i][0]
        if acum > orders[i][1]:
            max = -heapq.heappop(ans)
            acum -= max
    return len(ans)

def main():
    
    cases = int(stdin.readline().strip())
    k = 0
    
    while k < cases:
        blank = stdin.readline()
        n = int(stdin.readline().strip())
        orders = []
        i = 0
        for i in range(n):
            order = tuple(map(int, stdin.readline().strip().split()))
            orders.append(order)
        
        orders.sort(key = lambda x: x[1])
        print(customer(orders))
        if k < cases - 1:
            print()
        
        k += 1
        
main()