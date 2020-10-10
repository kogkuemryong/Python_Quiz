'''
for문을 이용하여 실행 결과와 같은 형태로 출력하는 프로그램을 작성해 보세요.
실행 결과

* * * * * * * *
*             *
*             *
*             *
*             *
*             *
*             *
* * * * * * * *
'''
for i in range(8):
    for j in range(8):
        if i == 0 or i == 7:
            print(len(str(j))*"*", end=" ")
        else:
            if j == 0 or j == 7:
                print("*", end= " ")
            else:
                print(" ", end= " ")
    print()

