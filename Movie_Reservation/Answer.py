

for i in range(1,21):
    if not i % 2 == 1: # i를 2로 나눈 나머지
        continue
    else:
        print('A'+str(i), end=' ')

print()
for i in range(1, 21):
    if i % 2 == 1:
        print('A' + str(i), end= ' ')

print()
for i in range(1,21)[::2]: # [::2] : 2칸씩 건너 뛰어서 사용
    print('A' + str(i), end=' ')

        # i : 1 => 1
        # i : 2 => 0
        # i : 3 => 1
        # i : 4 => 0



