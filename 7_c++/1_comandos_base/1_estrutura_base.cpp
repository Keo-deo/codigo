#include <iostream> // Biblioteca padrão para entrada/saída
#include <windows.h> // Necessário para o SetConsoleOutputCP que faz indentificar caracteres especiais como ´ ` ^ ~ ç

int main() {
    SetConsoleOutputCP(CP_UTF8);

    std::cout << "Olá, mundo!" << std::endl; // Comando de saída
    return 0; // Indica que o programa finalizou com sucesso
}