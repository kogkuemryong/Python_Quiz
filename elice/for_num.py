'''
1 1~100까지의 수 중에서 홀수와 홀수의 합을 실행 결과와 같이 출력하는 프로그램을 작성해 보세요.

실행 결과
1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 + 21 + 23 + 25 + 27 + 29 +
31 + 33 + 35 + 37 + 39 + 41 + 43 + 45 + 47 + 49 + 51 + 53 + 55 + 57 +
59 + 61 + 63 + 65 + 67 + 69 + 71 + 73 + 75 + 77 + 79 + 81 + 83 + 85 +
87 + 89 + 91 + 93 + 95 + 97 + 99 = 2500
'''

cnt = 0
for i in range(1, 100, 2):
    if i < 99:
        print(i ,end=" + ")
        cnt += i
    else:
        print(i, end= " = ")
        cnt +=i
print(cnt)
