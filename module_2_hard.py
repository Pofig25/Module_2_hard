number = int(input("Введите число от 3 до 20: "))
result = ''
if number < 3 or number > 20:
    print("Вы ввели неправильное значение")
else:
    for i in range(1, number):
        for j in range(i+1, number):
            if number % (i+j) == 0:
                result += str(i) + str(j)
print(result)
