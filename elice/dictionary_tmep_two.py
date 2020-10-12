# 연습문제 6-7
temp = {'월': 25.5, '화': 28.3, '수': 33.2, '목': 32.1, '금': 17.3, '토': 35.3, '일': 33.3}

days = []
for i in temp:
    if temp[i] >= 30 :
        days.append(i)

print('기온이 30˚ 이상인 요일 : ', end='')
for i in range(len(days)):
    print('%s' % days[i], end='')

    if i != len(days) - 1:
        print(', ', end='')
