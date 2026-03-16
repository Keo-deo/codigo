#include <windows.h>
#include <iostream>
#include <string>

int main() {
    SetConsoleOutputCP(CP_UTF8);
    std::string nome;
    int idade;

    std::cout << "qual o seu nome: ";
    std::getline(std::cin, nome);

    std::cout << "E sua idade?: ";
    std::cin >> idade;

    std::cout << "Bem vindo " << nome << " fiquei sabendo que voce tem " << idade << " anos de idade";


    return 0;
}