# 5주차 백준 문제 풀이 1712 손익분기점

import sys

a,b,c = map(int, sys.stdin.readline().split())
if c-b <= 0: print(-1)
else : print(a//(c-b) +1)
