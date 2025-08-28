

````markdown
# Gerador de Cadeias para Gramáticas Livres de Contexto (GLC)

Este projeto implementa um gerador de cadeias a partir de Gramáticas Livres de Contexto (GLC), utilizando a linguagem Python. A ferramenta permite simular derivações a partir do símbolo inicial de uma gramática e visualizar sentenças válidas da linguagem definida.

## Objetivo

Desenvolvido como parte dos estudos em Teoria da Computação, este projeto tem como objetivo reforçar o entendimento sobre gramáticas formais, regras de produção e geração de sentenças válidas.

## Tecnologias utilizadas

- Python 3.x
- Estruturas de dados (listas, dicionários)
- Manipulação de strings

## Funcionalidades

- Definição de uma gramática (variáveis, terminais, símbolo inicial e produções)
- Geração de cadeias válidas a partir do símbolo inicial
- Visualização do processo de derivação

## Exemplo de entrada (gramática)

Variáveis: S, A  
Terminais: a, b  
Inicial: S  
Produções:  
S → aA | b  
A → aS | bA | a

## Estrutura dos arquivos

projeto_GLC/  
├── carregar_gramatica.py       # Define a classe da gramática  
├── gerar_cadeia.py             # Contém a lógica de geração das cadeias  
├── main.py                     # Ponto de entrada do programa  
└── README.md                   # Documentação do projeto

## Como executar

1. Clone este repositório:

```bash
git clone https://github.com/kafu14/projeto_GLC.git
cd projeto_GLC
````

2. Execute o programa:

```bash
python main.py
```

3. Insira os elementos da sua gramática quando solicitado.

## Autor

* Elionilson Viana
* Estudante de Ciência da Computação
* [https://www.linkedin.com/in/elionilson-viana-075206326](https://www.linkedin.com/in/elionilson-viana-075206326)

## Licença

Este projeto é livre para fins de estudo e uso educacional.

