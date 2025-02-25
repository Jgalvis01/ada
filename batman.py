"""
Julian Andres Galvis
18/02/2025
batman
"""

from sys import stdin

class Villain:
    def __init__(self, name, powers, life):
        self.name = name
        self.powers = powers
        self.life = life

    def set_life(self, life):
        self.life = life
    def get_life(self):
        return self.life
    def get_powers(self):
        return self.powers
    
class Power:
    def __init__(self, name, power, calories):
        self.name = name
        self.power = power
        self.calories = calories
        self.used = False

    def get_power(self):
        return self.power
    def get_calories(self):
        return self.calories
    def get_name(self):
        return self.name
    def get_used(self):
        return self.used
    def set_used(self, used):
        self.used = used
"""
def batman(calories, powers, villains, i, j, mem):
    ans = None
    if (calories, i, j) in mem:
        ans = mem[(calories, i, j)]
    else:
        if calories < 0:
            ans = False
        elif calories >= 0 and  j == len(villains):
            ans = True
        elif powers[i].get_calories() > calories:
            ans = False
        else:
            if powers[i].get_name() in villains[j].get_powers():
                if not powers[i].get_used():
                    powers[i].set_used(True)
                    ans = batman(calories - powers[i].get_calories(), powers, villains, i + 1, j+1, mem) or batman(calories, powers, villains, i + 1, j, mem)

    mem[(calories, i, j)] = ans      
    return ans
"""
def batman(powers, villains, i, j, mem):
    ans = None
    if (calories, i, j) in mem:
        ans = mem[(calories, i, j)]
    else:
        if 

def main():
    x = stdin.readline().strip().split()
    powers = int(x[0])
    villains = int(x[1])
    calories = int(x[2])
    mem = {}
    while powers != 0 and villains != 0 and calories != 0:
        pows = []  
        vills = []
        
        for _ in range(powers):
            p = stdin.readline().strip().split()
            power = Power(p[0], int(p[1]), int(p[2]))
            pows.append(power)
        
        for _ in range(villains):
            v = stdin.readline().strip().split()
            vill_name = v[0]
            vill_life = int(v[1])
            powers_list = v[2].split(',')  
            powers_list = set(powers_list)
            vills.append(Villain(vill_name, powers_list, vill_life))
        
        if batman(pows, vills, 0, 0, mem) <= calories:
            print("Yes")
        else:
            print("No")
        
        x = stdin.readline().strip().split()
        powers = int(x[0])
        villains = int(x[1])
        calories = int(x[2])

main()