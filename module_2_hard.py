number = int(input("Введите число от 3 до 20: "))
result = str()
if number < 3 or number > 20:
    print("Вы ввели неправильное значение")
else:
    for i in range(number):
        for j in range(i):
            if i > 0 and j > 0 and number % (i+j) == 0:
                result += str(i) + str(j)
print(result)
