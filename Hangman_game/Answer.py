from random import *

words = ['apple', 'banana', 'orange']
word = choice(words) # choice 를 사용하면 리스트의 내용을 랜덤으로 하나 가져옴
# word = 'apple'
print('answer :' + word)

letters = '' # 사용자로부터 지금까지 입력받은 모든 알파벳

while True:
    print()
    succed = True
    for w in word: # a p p l e
        if w in letters:
            print(w, end=' ')
        else:
            print('_', end = ' ')
            succed = False
    print()

    if succed:
        print('Success')
        break

    letter = input('Input letter > :' )
    if letter not in letters:
        letters += letter

    if letter in word:
        print('Correct')
    else:
        print('Wrong')