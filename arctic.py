"""
Julian Andres Galvis
18/02/2025
Arctic Viruz
"""
from sys import stdin

def arctic(m,start,end):

    ans = None
    if start >= len(m):
        ans = ans or False
    else:
        if start == end:
                if m[start] == "A" or m[start] == "T":
                    ans = ans or True
        elif m[start] == "C":
            ans = ans or False
        elif m[start] == "G" and m[end] != "C":
            ans = ans or False
        elif m[start] == "T":
            ans = ans or False
        elif ((m[start] == "G" and m[end] == "C") or (m[start] == "C" and m[end] == "G")) and start + 1 == end:         
            ans = ans or False
        else:
            if start > end:
                for i in range(start, end - 1, -1):
                    print(m[i], end="")
                print()
                if m[end] == "C":
                    ans = ans or arctic(m, start, end + 1)
                if m[start] == "A":
                 ans = ans or arctic(m, start - 1, end)
                if m[start] == "A":
                    ans = ans or arctic(m, end, start - 1)
                if m[end] == "C" and m[start] == "G":
                    ans = ans or arctic(m, end +1, start - 1)
            else:
                for i in range(start, end+1):
                    print(m[i], end = "")
                print()

                if m[end] == "C":
                    ans = ans or arctic(m,start,end-1)
                if m[start] == "A":
                    ans = ans or arctic(m,start+1,end)
                if m[start] == "A":
                    ans = ans or arctic(m,end, start+1)
                if m[start] == "G" and m[end] == "C":
                    ans = ans or arctic(m,end -1, start + 1)

    return ans




def main():

    data = stdin.readline().strip()
    while data != '':
        data = list(map(str, data.split()))
        n = data[0]
        m = data[1]
        if m == "A" or m == "T":
            print("simple")
        elif arctic(m,0,len(m)-1):
            print("mutation")
        else:
            print("doomed")
            

        data = stdin.readline().strip()
        
main()