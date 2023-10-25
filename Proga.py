number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
operation = input("Введите математическую операцию: ")
if operation == "+":
    print(number_1+number_2)
elif operation == "-":
    print(number_1-number_2)
elif operation == "/":
    print(number_1/number_2)
elif operation == "*":
    print(number_1*number_2)
else:
    print("Error")
