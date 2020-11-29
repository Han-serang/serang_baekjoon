<<<<<<< HEAD
#3주차 백준 문제풀이 2869 입국심사

A, B, V = map(int, input().split())

high = V - A
if high % (A-B) == 0:
    first = int(high/(A-B))
else :
    first = int(high/(A-B)+1)
print(first+1)
=======
>>>>>>> parent of 43d671a (1주차 문제풀이 완료)
