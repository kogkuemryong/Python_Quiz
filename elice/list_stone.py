# 연습문제 5-7
stone = [[0, 0, 0, 0, 0, 0, 0, 0, 0], \
         [0, 1, 0, 1, 2, 1, 2, 1, 0], \
         [0, 2, 1, 1, 1, 2, 2, 0, 0], \
         [0, 0, 2, 2, 2, 1, 0, 2, 0], \
         [0, 0, 0, 0, 0, 1, 0, 2, 1], \
         [0, 0, 0, 2, 0, 1, 2, 1, 0], \
         [0, 0, 0, 2, 1, 0, 1, 1, 0], \
         [0, 0, 0, 1, 1, 0, 0, 0, 0], \
         [0, 0, 0, 0, 2, 2, 2, 0, 0]]

num_black = 0
num_white = 0

for i in range(0,9):
    for j in range(0,9):
        if stone[i][j] == 1:
            print('%3s' % '●', end='')
        elif stone[i][j] == 2:
            print('%3s' % '○', end='')
        else:
            print('%3s' % '×', end='')

    print()
