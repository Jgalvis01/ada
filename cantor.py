from sys import stdin

def cantor(number, low , high):
    ans = False
    precision = 1e-14
    if number == 1:
        ans = True
    elif number == 0:
        ans = True
    elif high - low < precision:
        ans = False
    else: 
        mid1 = low + (high - low) / 3
        mid2 = high - (high - low) / 3
        print (low, mid1, mid2, high)
        if number == mid1 or number == mid2 :
            ans = True
        elif number > mid1 and number < mid2:
            ans = False
        elif number < mid1:
            ans = cantor(number, low, mid1)      
        elif number > mid2:
            ans = cantor(number, mid2, high)

    return ans


def main():
    
    data = stdin.readline().strip()
    while data != "END":
        
        number = float(data)
        low = 0.0
        high = 1.0
        if cantor(number, low, high):
            print("MEMBER")
        else:
            print("NON-MEMBER")

        data = stdin.readline().strip()

main()