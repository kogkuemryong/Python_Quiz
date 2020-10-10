'''
for문을 이용하여 실행 결과와 같은 형태로 출력하는 프로그램을 작성해 보세요.
실행 결과

0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
0 1 2 3 4 5
'''

for i in range(6):
    for j in range(6):
        if j <= i:
            print(j, end=" ")
    print()
