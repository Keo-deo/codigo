def somar(n1,n2)
    n1 + n2
end

def subtrair(n1,n2)
    n1 - n2
end

def multiplicar(n1, n2)
    n1 * n2
end

def dividir(n1, n2)
    n1 / n2
end

#fucoes ↑
#gets   ↓

print "escolha uma operacao usando os simbolos
(+ = soma | - = subtração | * = multiplicação | / = divisão)"
escolha = gets.chomp

print "Digite o primeiro número: "
num1 = gets.chomp

print "Digite o segundo número:"
num2 = gets.chomp

if escolha == "+"
    puts somar(num1, num2)
  
elsif escolha == " "
else
end

