# 🐉 O Despertar dos Dragões: Da Arte ao Código

Bem-vindo ao Totem Interativo do meu futuro Ateliê de esculturas e desenhos! Este projeto nasceu de um insight antes de dormir: transformar a experiência sensorial das minhas obras físicas em um jogo textual em Python.

A lógica do menu traz uma memória afetiva da minha infância: a escolha das cores baseada nos palitinhos de picolé e forminhas coloridas que usávamos para fazer picolé caseiro.

---

## A Jornada de Evolução do Software


Abaixo, explico as decisões técnicas por trás de cada arquivo:

### 1. Versão Original (`jogo_dos_dragoes.py`)
*   **O que faz**: Apresenta as primeiras caixas de dragões (Severino, Compadecida e Pôr do Sol) com suas descrições sensoriais.
*   **Decisão Técnica**: Utiliza blocos de decisões simples com `if`, `elif` e `else`.
*   **Tratamento de Dados**: Aplicação de `.strip().capitalize()` para garantir que o sistema não quebre caso o usuário digite espaços ou letras maiúsculas/minúsculas fora do padrão.

### 2. Evolução para Dicionários (`dagoes_dicionarios.py`)
*   **Por que mudar?** Se o Ateliê crescesse, criar um `elif` para cada novo dragão deixaria o código gigantesco e difícil de manter.
*   **Decisão Técnica**: Substituição das condicionais por um **Dicionário Aninhado** (`dict`). Os dragões viraram estruturas de dados centralizadas.
*   **Novos Atributos**: Alinhado com a realidade de uma galeria de arte, adicionei os campos `material` e `status` (disponibilidade de venda), preparando o sistema para o gerenciamento de estoque real do Ateliê.

### 3. Implementação do Catálogo Geral (`dragoes_catalogo.py`)
*   **O que faz**: Permite que o visitante digite "Catalogo" para ver todas as obras expostas de uma só vez, sem precisar adivinhar as cores.
*   **Decisão Técnica**: Uso do loop `for` combinado com o método `.items()` para percorrer chaves e valores simultaneamente.
*   **Controle de Fluxo**: Uso do comando `continue` para reiniciar o menu de escolhas assim que a exibição do catálogo termina.

---

## Tecnologias Utilizadas
*   Python 3.14.6
*   VS Code (Ambiente de Desenvolvimento)

------
# Estrutura do Diagrama de Casos de Uso

ATOR PRINCIPAL: Visitante da Galeria

CASOS DE USO (As ações que o visitante faz):
1. [ Escolher Cor do Palitinho ]
2. [ Visualizar Obra e Experiência Sensorial ]
3. [ Solicitar Catálogo Completo ]
4. [ Sair da Exposição ]

REGRAS DO SISTEMA (O que acontece nos bastidores):
* O sistema padroniza o texto digitado pelo Visitante.
* Se a cor existir, o sistema busca os dados no Catálogo (Dicionário).
* Se a cor não existir, o sistema exibe uma dica nostálgica.
* 'Sair' encerra a execussão do progrma.
