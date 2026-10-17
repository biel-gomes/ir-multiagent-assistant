# Plano de construção do TCC

## Objetivo do protótipo

Construir uma ferramenta experimental e complementar para organizar dúvidas e revisar cenários fictícios de IRPF. A avaliação observará se o sistema identifica pendências e inconsistências e se apresenta fundamentos rastreáveis. Não se concluirá que a ferramenta reduz malha fina ou aumenta restituição sem um estudo apropriado.

Antes de codificar regras tributárias, delimitar o exercício fiscal, os tipos de situação atendidos, os dados de entrada e os casos de referência. Usar apenas dados fictícios.

## Arquitetura e responsabilidades

- **Flow:** mantém estado de cada execução, valida formatos, escolhe caminhos, faz chamadas às etapas e conduz pedidos de esclarecimento.
- **Agente 1 — interpretação da entrada:** organiza a dúvida e extrai informações fornecidas; identifica ambiguidades e perguntas pendentes. Pode ser ignorado quando a entrada já estiver estruturada.
- **Agente 2 — fundamentação tributária:** consulta a base RAG e relaciona trechos de fontes oficiais ao caso, informando origem e limites.
- **Funções Python:** conferem campos e formatos e executam cálculos definidos. Operações objetivas não ficam a cargo do LLM.
- **Agente 3 — revisão:** compara dados, fontes recuperadas e cálculos; entrega achados, justificativas e pendências sem criar regras.

## Etapas e critérios de aceite

### Planejamento — antes de `v0.1.0`

Definir um caso de uso inicial, quem o protótipo atende, que exercício fiscal será considerado, quais dados fictícios entram e quais resultados são esperados. Preparar Git, Python e CrewAI.

**Aceite:** escopo inicial escrito; cópia local sincronizada com o GitHub; ambiente usa uma versão de Python compatível.

### `v0.1.0` — Flow básico

Gerar a estrutura oficial de Flow pela CLI do CrewAI. Entender e executar a entrada, o estado, a validação e a apresentação no terminal. Não usar LLM nesta versão.

**Aceite:** execução completa com um exemplo fictício, instruções de instalação e execução, e explicação do papel de cada arquivo principal.

### `v0.2.0` — Interpretação da dúvida

Adicionar um Agente 1 com tarefa específica e saída estruturada. Configurar a LLM localmente, mantendo segredos fora do repositório.

**Aceite:** exemplos fictícios mostram interpretação consistente, campos extraídos e perguntas quando há ambiguidade.

### `v0.3.0` — Fundamentação por RAG

Selecionar fontes oficiais para o escopo; registrar órgão, título, exercício/versão e data de obtenção. Criar recuperação de trechos e integrar o Agente 2.

**Aceite:** respostas apontam para os trechos e fontes recuperados; consultas sem evidência suficiente são sinalizadas.

### `v0.4.0` — Validação e cálculos

Definir um formato estruturado para análise prévia. Implementar em Python as verificações e cálculos que cabem no escopo acordado.

**Aceite:** casos de referência têm resultados conferíveis; dados ausentes ou inválidos são identificados antes de gerar conclusão.

### `v0.5.0` — Revisão consolidada

Integrar o Agente 3 para comparar dados, fundamentos recuperados e resultados determinísticos. Padronizar um relatório com achados, evidências, recomendações e pendências.

**Aceite:** todo achado aponta para dado, fonte ou cálculo pertinente e o sistema distingue evidência de sugestão.

### `v0.6.0` — Interface de demonstração

Criar uma interface simples para consultar uma dúvida e executar uma análise prévia com dados fictícios. Mostrar perguntas, referências, falhas e relatório.

**Aceite:** demonstração de ponta a ponta reproduzível sem editar o código para cada caso.

### `v0.7.0` — Avaliação

Executar casos de referência com resultados esperados definidos previamente. Comparar saídas e documentar erros, acertos e limitações.

**Aceite:** procedimento e resultados reproduzíveis, com critérios explícitos; correções relevantes incluídas.

### `v1.0.0` — Consolidação

Revisar instalação limpa, documentação, interface e exemplos. Corrigir divergências entre TCC escrito e protótipo.

**Aceite:** versão demonstrável e documentação técnica coerente, com limitações claramente descritas.

## Organização prevista

A estrutura final aproveitará a gerada pela CLI oficial do CrewAI e manterá documentação separada:

```text
.
├── AGENTS.md
├── CHANGELOG.md
├── README.md
├── docs/
│   └── plano-de-construcao.md
├── knowledge/                 # fontes selecionadas e metadados
├── src/                       # Flow e código Python do sistema
├── tests/                     # testes de lógica e casos fictícios
├── .env.example               # nomes de variáveis, sem segredos
├── .gitignore
└── pyproject.toml              # dependências e comandos CrewAI
```

Não criar uma pasta completa por versão. Cada tag aponta para o estado cumulativo do código naquele marco.

## Rotina de aprendizagem e versão

Para cada marco: ler o critério de aceite; entender entradas, saídas e fluxo; implementar uma parte pequena; executar e interpretar o resultado; testar um caso esperado e um caso inválido; revisar as mudanças e segredos; atualizar documentação; então fazer commit e tag. O assistente explica e revisa, e só edita arquivos locais quando solicitado.

Use `main` para estados estáveis e uma branch de funcionalidade durante trabalho maior. Commits podem registrar o progresso, mas uma tag de versão só deve ser criada depois que o aceite estiver verificado.

## Ambiente atual

Em 17/10/2026, no computador de desenvolvimento: Git 2.55.0, uv 0.13.1, Python 3.12.15 gerenciado pelo uv e CLI CrewAI 1.15.28. O Python 3.14.8 também permanece instalado, mas não atende ao intervalo exigido pelo CrewAI (Python >=3.10 e <3.14). O ambiente virtual do projeto será criado quando a estrutura CrewAI estiver na pasta do repositório.
