#include <windows.h>
#include <iostream>
#include <string>

int main() {
    SetConsoleOutputCP(CP_UTF8);
    int numero = 10;

    std::cout << "Contagem regresiva";
    while (numero != -1) // para parar o loop é so usar o break que nem no python
    {
        std::cout << "\n" << numero;
        numero -= 1;
    }
    return 0;
}