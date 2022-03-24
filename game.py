from random import randint

number =  randint(0,512)
k=0
while True:
    pidor = int(input('Введите число'))
    if pidor>number:
        k+=1
        print('Загаданое число меньше')
    elif pidor<number:
        k+=1
        print('Загаданое число больше')
    elif pidor == number:
        print('Вы отгадали число! \nКоличество выших попыток составило ' + str(k))
        break

input()