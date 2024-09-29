# Sistema Bancário em Python 🏦

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg) 
![pytz](https://img.shields.io/badge/Library-pytz-lightgrey.svg) 
![random](https://img.shields.io/badge/Library-random-lightgrey.svg)
![datetime](https://img.shields.io/badge/Library-datetime-lightgrey.svg)

## Descrição do Projeto

Este sistema bancário foi desenvolvido como parte do **Curso de Engenharia de Dados 2024**, promovido pelo **Santander Coders** em parceria com a **Ada Tech**. O objetivo principal deste projeto é simular operações básicas de um banco, como criação de contas, depósitos, saques e consulta de extrato, utilizando conceitos fundamentais de Python, estrutura de dados e controle de fluxo.

## Funcionalidades

- **Criar Usuário**: Permite a criação de um novo usuário com CPF, nome, data de nascimento e endereço.
- **Criar Conta Corrente**: Gera uma conta corrente associada a um CPF existente.
- **Depósito**: Realiza depósitos na conta selecionada, limitados a 10 operações por dia.
- **Saque**: Efetua saques, verificando o saldo disponível e o limite diário de transações.
- **Extrato**: Exibe as últimas 5 transações, com data, tipo e valor.

## O que Aprendi

Durante o desenvolvimento deste sistema, apliquei diversos conceitos e práticas aprendidos nas trilhas de **Fundamentos de Python** e **Estrutura de Dados em Python**:

1. **Controle de Fluxo**: Utilizei loops (`while`, `for`) e condições (`if`, `else`) para gerenciar o menu interativo e validar operações bancárias.
2. **Estrutura de Dados**: Implementei dicionários e listas para armazenar informações dos usuários, contas e transações de forma estruturada e eficiente.
3. **Manipulação de Datas e Horários**: Com o uso da biblioteca `pytz`, manipulei fuso horários para garantir que as operações fossem registradas corretamente de acordo com a zona de Fortaleza.
4. **Modularidade**: O código foi organizado em funções que permitem maior clareza e reuso, seguindo boas práticas de desenvolvimento.

## Tecnologias Usadas

- [Python](https://www.python.org/) - Linguagem principal do projeto.
- [pytz](https://pypi.org/project/pytz/) - Biblioteca para manipulação de fusos horários.
- [datetime](https://docs.python.org/3/library/datetime.html) - Biblioteca padrão para manipulação de datas.
- [random](https://docs.python.org/3/library/random.html) - Utilizada para gerar números aleatórios para contas bancárias.

## Como Executar o Projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/seuusuario/sistema-bancario-python.git
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute o sistema:
    ```bash
    python sistema_bancario.py
    ```

## Sistema Bancário em Python

![Banco de Dados Python](https://media.licdn.com/dms/image/v2/D4D12AQF9KT1ofTmh_w/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1703861831035?e=1733356800&v=beta&t=DcUyhazw6WJgWN8iSL2Ob_m5CtNvzlXbwMJQIuNDBNE)

## Contato

- **Teophilo Silva** - [LinkedIn](https://www.linkedin.com/in/teophilo-silva-dev)
- Email: teophilo@gmail.com
