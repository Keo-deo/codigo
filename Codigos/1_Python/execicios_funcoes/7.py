def calculadora(n1 ,n2, operacao):
    if operacao == "+":
        return n1 + n2
    elif operacao == "-":
        return n1 - n2
    elif operacao == "*":
        return n1 * n2
    elif operacao == "/":
        return n1 / n2
    else:
        return "Operação inválida."
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
oper = input("Digite a operação (+, -, *, /): ")
print(f"O resultado é: {calculadora(num1, num2, oper)}")