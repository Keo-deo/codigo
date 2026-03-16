#include <windows.h> // Necessário para o SetConsoleOutputCP que faz indentificar caracteres especiais como ´ ` ^ ~ ç
#include <iostream> // Biblioteca padrão para entrada/saída
#include <string>

int main() {
    SetConsoleOutputCP(CP_UTF8);
    int qtd, numero;

    std::cout << "digite um numero: ";
    std::cin >> qtd;

    for(int i=qtd; i!=-1; i--){
        std::cout << "\n" << i;

    }
    return 0; // Indica que o programa finalizou com sucesso
}