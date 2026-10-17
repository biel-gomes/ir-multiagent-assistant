# Instruções de colaboração

## Objetivo de ensino

Gabriel quer programar e entender cada etapa. Explique o que será construído, quais arquivos serão afetados e quais conceitos novos aparecem. Oriente e revise primeiro; altere arquivos diretamente somente quando ele pedir.

## Ciclo de trabalho

1. Leia o marco correspondente em `docs/plano-de-construcao.md`.
2. Explique o objetivo e proponha um exercício pequeno.
3. Ajude a implementar e entender o código em partes.
4. Oriente a execução e os testes; explique cada erro.
5. Só considere o marco concluído quando os critérios de aceite forem atendidos.
6. Ajude a registrar README, CHANGELOG, commit e tag depois de Gabriel revisar as mudanças.

## Regras técnicas

- Siga a documentação oficial e a versão instalada do CrewAI; confira detalhes sujeitos a mudanças.
- Use Flow para estado, sequência, roteamento e validações previsíveis.
- Use Python para cálculos e verificações determinísticas.
- Use agentes para tarefas interpretativas delimitadas; defina entradas e saídas estruturadas.
- Preserve as fontes recuperadas pelo RAG e deixe explícita a falta de evidência.
- Prefira código simples, funções curtas e nomes claros em português.
- Evite dependências e infraestrutura sem necessidade demonstrada.

## Segurança e avaliação

- Use somente dados fictícios; não envie declarações ou identificadores reais ao modelo.
- Nunca registre chaves, tokens, arquivos `.env` ou dados fiscais reais no Git.
- Não prometa prevenção de malha fina ou aumento de restituição.
- Registre escopo, casos de referência, falhas conhecidas e limitações.

## Git

- Mantenha `main` executável.
- Use branches de funcionalidade quando fizer sentido e commits pequenos.
- Crie tags `vX.Y.Z` somente para versões testadas e demonstráveis.
- Não reescreva histórico nem faça force push.
