#include <windows.h>
#include <iostream>
#include <string> // biblioteca para atribuir srings (mais de um caractere)

int main() {
    SetConsoleOutputCP(CP_UTF8);
    
    std::string nome = "murilo";// armazena multiplos caracteres

    int myint = 10; // numeros inteiro
    unsigned myunsigned = 0; // numero inteiro que nao pode ser negativo
    float myfloat = 1.0f;// numeros decimais
    double mydouble = 1.0;//numeros decimais

    bool mybool = true; // true e false
    char mychar = 'a' ;// guarda um caracter seja um letra como "a" ou um numero "9"
    //precisa ser com aspas simples ''

    // da pra mudar o valor no meio do codigo
    //Ex:
    myint = 13;

    return 0;
}