number = int(input("Введите число: "))
power_of_two = 0
answer = 0
while 2 ** power_of_two < number:
    print(2 ** power_of_two, end=' ')
    power_of_two += 1