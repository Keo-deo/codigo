require 'tty-prompt'

prompt = TTY::Prompt.new

fruta = prompt.select("Selecione uma fruta:") do |menu|
  menu.choice 'Maca'
  menu.choice 'Banana'
  menu.choice 'Mamao'
end

puts "Voce selecionou: #{fruta}"

prompt = TTY::Prompt.new
escolha = prompt.select("Qual sua linguagem favorita?", %w(Ruby Python JavaScript))

puts "Você escolheu #{escolha}!"