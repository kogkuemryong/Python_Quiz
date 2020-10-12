# 연습문제4-10
print('-' * 40)
print('      cm      mm        m       inch')
print('-' * 40)

cm = 1
while cm < 99:
    for cm in range(1,100,2):
        mm = cm * 10
        m = cm * 0.01
        inch = cm * 0.3937
        print('%8d %8d %8.2f %8.2f' % (cm, mm, m, inch))



print('-' * 40)
