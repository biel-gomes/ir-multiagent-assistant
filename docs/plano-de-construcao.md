# Plano de construção do projeto

## Propósito

Construir um protótipo acadêmico, em etapas curtas, que auxilie a organizar informações e revisar casos de IRPF com base em fontes oficiais. O foco da avaliação é a qualidade da assistência em cenários de teste; o projeto não poderá concluir que reduz a malha fina sem evidências apropriadas.

O escopo tributário, o exercício fiscal e os casos atendidos serão definidos antes de integrar legislação ou fazer cálculos. Até essa definição, todos os dados usados serão fictícios.

## Papéis da arquitetura

- **Flow:** mantém o estado de uma execução, valida formatos, escolhe caminhos, chama funções determinísticas e encaminha os dados.
- **Agente 1 — interpretação da entrada:** transforma uma dúvida em dados organizados e aponta ambiguidades. O Flow pode pular este agente quando a entrada já vier estruturada.
- **Agente 2 — fundamentação tributária:** consulta fontes selecionadas por RAG e explica quais regras podem se aplicar, sempre preservando a referência da fonte.
- **Funções Python:** calculam valores e verificam condições expressas em regras implementadas. Não delegar aritmética ou checagens objetivas a um LLM.
- **Agente 3 — revisão:** compara os dados, as fontes recuperadas e os resultados das funções; produz apontamentos explicados, sem inventar regras.

## Versões e critérios de aceite

| Marco | Implementação | Critério de aceite | Registro |
|---|---|---|---|
| Planejamento | Delimitar público, casos, exercício fiscal, dados, fluxo e critérios de avaliação. Preparar o ambiente de desenvolvimento e entender Git básico. | Escopo aprovado para começar; repositório clonado e sem segredos; cada caso de uso tem entrada e resultado esperado. | Commit da documentação; sem tag de software. |
| `v0.1.0` | Criar o Flow pela CLI oficial do CrewAI. Implementar entrada simples, estado, validação e saída no terminal. | Instalação e execução documentadas; exemplo fictício percorre todo o fluxo; estudante consegue explicar cada método. | README, CHANGELOG, commit e tag. |
| `v0.2.0` | Configurar o provedor de LLM localmente e adicionar o Agente 1 para interpretar dúvidas e retornar campos estruturados e pendências. | Pelo menos três entradas fictícias produzem saída compatível com o formato definido; ambiguidade gera pergunta ou pendência explícita. | Atualizar exemplos e limitações; tag. |
| `v0.3.0` | Selecionar fontes oficiais do escopo e criar recuperação RAG; integrar o Agente 2 ao Flow. | Consulta mostra trechos recuperados e referência; pergunta fora da base recebe indicação de insuficiência, sem regra inventada. | Registrar fontes, data/versão, procedimento de atualização e tag. |
| `v0.4.0` | Criar funções Python para validações e cálculos dentro do escopo definido; aceitar uma entrada estruturada de análise prévia. | Casos conhecidos retornam resultados conferíveis; dados incompletos ou inválidos são sinalizados sem produzir conclusão enganosa. | Adicionar casos de teste fictícios, documentação e tag. |
| `v0.5.0` | Integrar o Agente 3 para revisar a coerência e gerar um relatório de achados, evidências e pendências. | Cada achado aponta para dado, regra recuperada ou cálculo; o relatório separa evidência de recomendação. | Exemplo completo, limitações e tag. |
| `v0.6.0` | Criar interface simples para consulta e análise prévia; apresentar perguntas e relatório de modo claro. | Demonstração ponta a ponta com dados fictícios; erros e ausência de fontes são visíveis ao usuário. | Instruções de execução e tag. |
| `v0.7.0` | Avaliar casos de referência e corrigir problemas encontrados. Comparar saídas do sistema com respostas esperadas revisadas. | Critérios, casos, acertos, erros e limitações registrados de forma reproduzível. | Relatório de avaliação e tag. |
| `v1.0.0` | Consolidar o protótipo demonstrável e a documentação técnica para o TCC. | Instalação limpa e demonstração reproduzíveis; documentação corresponde ao código e aos resultados. | Release/tag final e notas da versão. |

O cronograma de semanas será definido após o planejamento e uma medição simples do tempo gasto em `v0.1.0`. As estimativas iniciais de esforço por etapa são hipóteses, não prazos garantidos.

## Caminho de aprendizagem por etapa

Para cada versão, seguir este ciclo:

1. **Entender:** ler o critério de aceite e identificar os conceitos novos.
2. **Desenhar:** registrar entrada, saída, arquivos afetados e caminho dos dados.
3. **Programar:** escrever em pequenos trechos, executando após cada mudança.
4. **Explicar:** descrever o que cada função, classe ou configuração faz.
5. **Verificar:** testar o caso feliz, uma entrada inválida e um caso de limite relevante.
6. **Versionar:** revisar diff e segredos, atualizar documentação, fazer commit e tag ao cumprir o aceite.

O assistente deve primeiro orientar e revisar. Intervenção direta nos arquivos fica para quando o estudante solicitar.

## Regras para versões independentes

Cada versão será cumulativa e executável sozinha a partir de um clone limpo. Não manter cópias completas do programa em pastas separadas. Uma tag Git identifica exatamente o código de uma versão anterior e permite recuperá-lo.

Uma versão só é considerada concluída quando houver:

- comandos de instalação e execução testados ou uma limitação registrada;
- exemplo de demonstração com entrada fictícia;
- critério de aceite verificado;
- README e CHANGELOG atualizados;
- commit identificável e tag da versão.

## Fluxo de GitHub

- `main` recebe versões concluídas e documentação revisada.
- Para construir uma funcionalidade, abrir uma branch como `feat/agente-interpretacao`.
- Fazer commits pequenos enquanto se trabalha.
- Integrar a branch em `main` quando a versão passar pelos critérios de aceite.
- Criar uma tag `vX.Y.Z` no commit da versão pronta.
- Para retomar em outro computador, clonar o repositório e selecionar a tag ou branch desejada.

## Segurança e limites

- Usar apenas exemplos inventados; não subir declaração real ou documento fiscal.
- Guardar chaves no arquivo local `.env`, ignorado pelo Git, e fornecer apenas nomes de variáveis em `.env.example`.
- Não usar a LLM para cálculo financeiro ou para substituir regras explícitas de validação.
- Preservar fontes e trechos usados; informar quando não houver base suficiente.
- Tratar o resultado como apoio experimental, sem promessa de evitar malha fina ou elevar restituição.
