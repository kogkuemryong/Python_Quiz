# 연습문제 6-6
temp = {'월': 25.5, '화': 28.3, '수': 33.2, '목': 32.1, '금': 17.3, '토': 35.3, '일': 33.3}

a = min(temp)

for i in temp:
    if i == min(temp):
        print('가장 낮은 최고 기온 : %6.1f˚' % temp[i])
