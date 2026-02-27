#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main()
{
    int contador, qtd_materias;
    float soma;
    struct Aluno
    {
        char nome[51];
        float media;
    };

    struct Aluno MeuAluno;

    printf("Digite o nome do aluno: ");
    fgets(MeuAluno.nome, 51, stdin);
    MeuAluno.nome[strcspn(MeuAluno.nome, "\n")] = 0;
    printf("Voce deseja calcular a media de quantas materias: ");
    scanf("%d", &qtd_materias);
    float notas[qtd_materias];

    soma = 0;
    for (contador = 0; contador < qtd_materias; contador++)
    {
        printf("\nDigite a nota da %d materia do aluno %s: ", contador+1, MeuAluno.nome);
        scanf("%f", &notas[contador]);
        soma = soma + notas[contador];
    }//for
        
    MeuAluno.media = soma / qtd_materias ;
    
    FILE *arquivo;
    arquivo = fopen("notas_alunos.txt", "w");

    if (MeuAluno.media >= 6) {

        if (arquivo == NULL) {
            printf("erro ao abrir o arquivo");
            return 1;
        }
        fprintf(arquivo, "relatorio de media das materias:\n");
        fprintf(arquivo, "Nome do aluno: %s",MeuAluno.nome);
        fprintf(arquivo, "status: Aprovado!!", MeuAluno.media);
        fclose(arquivo);

        printf("\n dados salvos com sussesso em ''notas_alunos.txt''!");}// if (MeuAluno.media >= 6)

    else {
        if (arquivo == NULL) {
            printf("Erro ao abrir o arquivo");
            return 1;
        }
        fprintf(arquivo, "relatorio de media das materias:\n");
        fprintf(arquivo, "Nome do aluno \n: %s",MeuAluno.nome);
        fprintf(arquivo, "status: Reprovado", MeuAluno.media);

        printf("\n dados salvos com sussesso em ''notas_alunos.txt''!");
        printf("\nOBS: pessimas noticias");}
    fclose(arquivo);
    return 0;
}//main