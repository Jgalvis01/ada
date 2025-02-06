from sys import stdin

def calculate_v(V, L, K, T1, T2):
    
    rate = V / T1
    time_to_reach_L = L / rate  

    if time_to_reach_L >= T1:
        final_height = V
    else:    
        height_after_rain = L + (rate - K) * (T1 - time_to_reach_L)
        final_height = max(L, height_after_rain - K * T2)

    return final_height

def find_V(L, K, T1, T2, H, find_min):
    ans = 0
    low, high = H, 1e7
    for _ in range(100): 
        mid = (low + high) / 2
        if calculate_v(mid, L, K, T1, T2) <= H:
            low = mid
        else:
            high = mid
    
    
    if find_min:
        if L == H:
            ans = L
        else:
            ans = (low + high) / 2
    else:
        ans = high
    
    return ans


def main():
    
    N = int(input())
    for _ in range(N):
        L, K, T1, T2, H = map(float, input().split())
        F1 = find_V(L, K, T1, T2, H, find_min=True)
        F2 = find_V(L, K, T1, T2, H, find_min=False)
        print(f"{F1:.6f} {F2:.6f}")
    
main()
