import math

if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        dist = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
        if dist == 0 and r1 == r2:
            print(-1)
        elif dist == r1 + r2 or dist == abs(r2 - r1):
            print(1)
        elif r1 + r2 > dist and dist > abs(r2 - r1):
            print(2)
        else:
            print(0)