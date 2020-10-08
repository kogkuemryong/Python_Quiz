# a = int(input())
#
# for i in range(a):
#     b = str(input())
#     s = list(b)
#     sum = 0
#     c = 1
#     for i in s:
#         if i == "O":
#             sum += c
#             c += 1
#         else:
#             c = 1
#     print(sum)

a = int(input())

for i in range(a):
    b = str(input())
    s = list(b)
    sum = 0
    cnt = 1
    for i in s:
        if i == "O":
            sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum)
