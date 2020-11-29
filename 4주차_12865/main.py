# 4주차 백준 문제 풀이 12865 평범한 배낭

n,k = map(int, input().split(' '))
_map = [  [0]*(k+1) for _ in range(n+1) ]

for i in range(1, n+1):
    w,v = map(int, input().split('  '))
    for j in range(1, k+1):
        if j <w:
            _map[i][j] = _map [i-1][j]
        else :
            _map[i][j] = max(_map[i-1][j], _map[i-1][j-w] + v)
print(_map[n][k])