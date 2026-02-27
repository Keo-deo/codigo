print "Digite seu nome:"
nome = gets.chomp
print "Digite a sua idade:"
idade = gets.chomp.to_i

tempo_para_aposentadoria = 65 - idade
ano_de_aposentadoria = 2026 - idade + 65

puts "\nOlá, #{nome}. Faltam #{tempo_para_aposentadoria} anos para você se aposentar.
e isso será no ano de #{ano_de_aposentadoria}."
