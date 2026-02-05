#include <stdio.h>
#include <stdlib.h>

int main()
{
    char sair, operacao;
    float n1, n2;

    while (1) {
        system("cls");
        printf("escolha um numero: ");
        scanf("%f", &n1);

        printf("escolha uma operacao\n ( + | - | * | / ) \n");
        scanf(" %c", &operacao);

        printf("escolha o segundo numero: ");
        scanf("%f", &n2);

        switch (operacao) {
            case '+':
                printf("\n %.2f + %.2f = %.2f", n1, n2, n1 + n2);
                break;

            case '-':
                printf("\n %.2f - %.2f = %.2f", n1, n2, n1 - n2);
                break;

            case '*':
                printf("\n %.2f X %.2f = %.2f", n1, n2, n1 * n2);
                break;

            case '/':
                if (n2 == 0) {
                    printf("\nErro: Divisao por zero");
                    break;}
                else {
                    printf("\n %.2f / %.2f = %.2f", n1, n2, n1 / n2);}
                break;

            default:
                printf("escolha uma operacao dentre as opcoes");}//switch

        printf("\nDeseja encerrar o programa? (s, S, n ou N) ");
        scanf(" %c", &sair);

        if (sair == 's' || sair == 'S') {
            printf("Encerrando programa...");
            break;}

    }//while
    return 0;
}//main