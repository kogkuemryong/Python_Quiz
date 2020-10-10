'''
N을 입력 받아 다음과 같은 수식의 결과를 얻는 프로그램을 작성해 보세요.
{2}^{1} + {4}^{3} + {6}^{5} + … + {2N}^{(2N-1)}2
1
 +4
3
 +6
5
 +…+2N
(2N−1)
프로그램을 실행하여 N의 값을 12로 입력해 보세요.
'''

n = int(input('N의 값을 입력하세요 : '))
sum = 0

for i in range(n+1):
    if i % 2 == 0 and i != 0:
        num = i ** (i - 1)
        sum += num

print('N의 값 : %d' % n)
print('합계 : %d' % sum)
