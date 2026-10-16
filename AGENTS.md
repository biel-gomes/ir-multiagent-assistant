# Instruções para trabalhar neste repositório

## Objetivo

Este repositório contém o protótipo de TCC sobre assistência à análise de declarações de IRPF. O estudante quer programar e entender cada etapa. Ensine antes de assumir a implementação.

## Como conduzir cada etapa

1. Consulte o plano no README e em `docs/plano-de-construcao.md`.
2. Explique o objetivo, os arquivos a criar ou alterar e os conceitos necessários.
3. Oriente o estudante a escrever uma parte pequena do código. Dê exemplos curtos quando ajudarem.
4. Revise o que foi escrito, explique erros e proponha o próximo exercício.
5. Só altere os arquivos diretamente quando o estudante pedir intervenção.
6. Ao concluir um marco, atualize a documentação da versão e ajude a registrar commit e tag.

## Regras técnicas

- Siga a versão instalada do CrewAI e a documentação oficial atual. Confira APIs sensíveis à versão; não invente padrões.
- Prefira construções Python simples, nomes em português e funções curtas.
- Use o Flow para estado, sequência, decisões, validações previsíveis e chamadas a cálculos Python.
- Use agentes apenas para tarefas interpretativas bem delimitadas. Evite agentes para validações determinísticas.
- Defina entradas e saídas estruturadas entre etapas. Preserve a origem das regras usadas no RAG.
- Cada versão deve partir da anterior, funcionar de ponta a ponta e incluir instruções de execução e limitações.
- Não adicione bibliotecas, abstrações ou infraestrutura antes de justificar sua necessidade.

## Dados e segurança

- Use dados inteiramente fictícios nos exemplos, testes e demonstrações.
- Nunca inclua chaves de API, arquivos `.env`, declarações reais ou identificadores pessoais no Git.
- Mantenha `.env.example` sem valores secretos e confira `.gitignore` antes de qualquer commit.
- Não afirme que o protótipo garante restituição maior ou evita malha fina.
- Indique quando uma resposta não tiver suporte suficiente nas fontes recuperadas.

## Git e versões

- Faça commits pequenos com mensagens que expliquem a mudança.
- Use branches de trabalho quando houver uma funcionalidade em desenvolvimento; mantenha `main` executável.
- Crie tags `vMAJOR.MINOR.PATCH` apenas para marcos executáveis e demonstráveis.
- Atualize README e CHANGELOG ao concluir uma versão.
- Nunca force push nem reescreva histórico sem instrução explícita.
