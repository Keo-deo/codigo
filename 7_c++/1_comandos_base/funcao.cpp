#include <windows.h>
#include <iostream>
#include <string>
/*
tipo de retono nome argumentos e escopo{}*/ 
void idade(int data, std::string nome) {
    int idade;

    idade = 2026 - data;
    
    std::cout << nome << " tem " << idade << " anos de idade";
}

int main() {
    SetConsoleOutputCP(CP_UTF8);
    int ano;
    std::string nome;
    
    std::cout << "digite seu nome: ";
    std::getline(std::cin, nome);

    std::cout << "digite o ano que voce nasceu: ";
    std::cin >> ano;

    idade(ano, nome);
    return 0;
}