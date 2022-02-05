# calculadora em python

print("***************************************** Python Calculator ****************************************************\n")

print("Selecione o número da operação desejada:\n")
print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n")
i = int(input("Digite sua opção (1/2/3/4): "))
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

if i == 1:
    print(num1, "+", num2, "=", int(num1) + int(num2))
elif i == 2:
    print(num1, "-", num2, "=", int(num1) - int(num2))
elif i == 3:
    print(num1, "*", num2, "=", int(num1) * int(num2))
elif i == 4:
    print(num1, "/", num2, "=", int(num1) / int(num2))
else:
    print("Opção Inválida!")