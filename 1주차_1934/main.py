#1주차 백준 문제풀이 1934 최소공배수

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    x = a
    y = b
    while b != 0:
        r = a % b
        a = b
        b = r
    gcd = a
    lcd = x * y / a
    print(int(lcd))