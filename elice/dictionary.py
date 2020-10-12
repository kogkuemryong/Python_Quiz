# 연습문제 6-3
data = {'kim99': 12000, 'lee66':11000, 'han55':3000, 'hong77':5000, 'hwang33':18000}

data['jang88'] = 7000.
print('전체 딕셔너리 : %s' % data)

for i in data :
    if i  == 'jang88':
        print('%s님의 마일리지(%d점)가 추가 되었습니다.' % ('jang88', data[i]))
