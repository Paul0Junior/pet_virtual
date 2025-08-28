# Pet Virtual em Python

# Pet Virtual em Python (Tamagotchi)

## Descrição do Projeto

Este é um jogo simples de simulação de pet virtual, no estilo Tamagotchi, desenvolvido em Python. O objetivo principal deste projeto foi aplicar de forma prática os conceitos fundamentais da Programação Orientada a Objetos (POO).

No jogo, o usuário pode escolher uma espécie (Gato ou Cachorro), dar um nome ao seu pet e interagir com ele através de um menu de ações para cuidar de suas necessidades básicas, como fome e energia.

## Funcionalidades

- **Criação de Pets:** O usuário pode dar um nome e escolher a espécie do seu pet (Gato ou Cachorro).
- **Interação via Menu:** Um loop interativo permite que o usuário escolha ações para o pet.
- **Gerenciamento de Atributos:** O pet possui atributos de `fome` e `energia` que mudam de acordo com as ações realizadas.
- **Ações Específicas:** Cada espécie possui uma ação única (miar para o Gato, latir para o Cachorro) que é executada na despedida.
- **Comportamentos Únicos:** A ação de "brincar" tem um efeito diferente para o Gato, demonstrando a sobrescrita de métodos.

## Como Rodar o Projeto

1.  **Pré-requisitos:** É necessário ter o Python 3 instalado em sua máquina.
2.  **Execução:** Salve o código em um arquivo (ex: `tamagotchi.py`) e execute o seguinte comando no seu terminal:
    ```bash
    python tamagotchi.py
    ```
3.  Siga as instruções que aparecerão no terminal para interagir com seu pet.

## Conceitos de POO Aplicados

Este projeto foi uma ferramenta de aprendizado para os seguintes pilares da Programação Orientada a Objetos:

-   **Classes e Objetos:** A classe `Pet` serve como um "molde" geral, enquanto as classes `Gato` e `Cachorro` são moldes mais específicos. O `meu_pet` criado no jogo é o objeto, ou seja, a instância concreta de uma dessas classes.

-   **Atributos e Métodos:** Os pets possuem **atributos** (características como `nome`, `fome`, `energia`) e **métodos** (comportamentos como `brincar()`, `comer()`, `dormir()`).

-   **Encapsulamento:** A lógica e os dados do pet estão contidos dentro da sua própria classe, mantendo o código organizado e coeso.

-   **Herança:** As classes `Gato` e `Cachorro` herdam todos os atributos e métodos da classe `Pet`, reutilizando código e criando uma hierarquia lógica.

-   **Polimorfismo (via Sobrescrita de Método):** O método `brincar()` da classe `Pet` foi sobrescrito na classe `Gato` para ter um comportamento diferente. Isso permite que objetos de tipos diferentes respondam à mesma chamada de método de maneiras únicas.
