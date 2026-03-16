#include <windows.h>
#include <iostream>
#include <string>

int main() {
    SetConsoleOutputCP(CP_UTF8);
    int numero;

    std::cout << "digite um numero para saber se ele é par ou nao: ";
    std::cin >> numero;

    if (numero % 2 == 0) {
        std::cout << numero << " é Par!!";
    }
    else {
        std::cout << numero << " é impar!!";
    }
    return 0;
}