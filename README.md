# Criação de lista sem números duplicados em Python

Projeto de estudo desenvolvido em Python que permite ao usuário criar uma lista de números inteiros sem valores duplicados. O programa valida a entrada do usuário, impede a repetição de números e exibe a lista final em ordem crescente.

## Objetivo do projeto

Praticar conceitos fundamentais da linguagem Python, como:

- Entrada de dados pelo terminal
- Estrutura de repetição `while`
- Estruturas condicionais `if`, `elif` e `else`
- Criação e manipulação de listas
- Verificação de valores com `in`
- Tratamento de erros com `try` e `except`
- Controle de fluxo com `continue` e `break`
- Ordenação de listas com `sorted()`

## Funcionalidades

O programa permite:

- Solicitar números inteiros ao usuário
- Validar se o valor digitado é um número inteiro
- Exibir uma mensagem caso o usuário digite letras ou outros valores inválidos
- Verificar se o número informado já existe na lista
- Impedir a adição de números duplicados
- Adicionar novos valores válidos à lista
- Perguntar se o usuário deseja continuar inserindo números
- Encerrar o programa quando o usuário escolher sair
- Exibir a lista final em ordem crescente

## Tecnologias utilizadas

- Python 3

## Como executar

Certifique-se de que o Python 3 está instalado no computador.

Baixe este repositório e execute o arquivo pelo terminal ou por uma IDE de sua preferência.

## Exemplo de Uso

Digite um valor: 8
Valor adicionado com sucesso
Quer continuar? S/N: S

Digite um valor: 4
Valor adicionado com sucesso
Quer continuar? S/N: S

Digite um valor: 8
Esse número já existe e está duplicado, portanto, não foi adicionado
Quer continuar? S/N: S

Digite um valor: abc
Digite somente valores inteiros para formar sua lista.

Digite um valor: 10
Valor adicionado com sucesso
Quer continuar? S/N: N

Você criou a lista: [4, 8, 10]
