# Assistente de apoio à análise do IRPF

Projeto de TCC em Ciência da Computação na UFABC. O objetivo é construir, por etapas, um protótipo que organize dúvidas e apoie a revisão de casos fictícios de IRPF, com regras fundamentadas em fontes oficiais.

O programa será complementar e experimental. Não substitui os sistemas ou orientações da Receita Federal e não promete evitar malha fina nem aumentar restituição.

## Como o projeto será construído

O estudante escreve e executa cada parte para aprender. A assistência explica conceitos, revisa o código e intervém nos arquivos somente quando solicitada.

- **Flow e Python:** controlam a sequência, o estado, validações objetivas e cálculos.
- **Agente 1 — interpretação:** organiza dúvidas em linguagem natural e identifica o que precisa ser esclarecido.
- **Agente 2 — fundamentação:** recupera fontes oficiais pelo RAG e explica quais regras podem se aplicar.
- **Agente 3 — revisão:** verifica coerência entre dados, fontes e resultados e apresenta achados justificados.

## Plano de versões

| Versão | Entrega funcional |
|---|---|
| Planejamento | Escopo, casos de uso, arquitetura e critérios de avaliação definidos. |
| `v0.1.0` | Flow básico executável, com entrada fictícia, estado e validação. |
| `v0.2.0` | Agente 1 interpreta dúvidas e retorna dados e pendências estruturados. |
| `v0.3.0` | Agente 2 consulta fontes oficiais por RAG e retorna referências. |
| `v0.4.0` | Funções Python validam dados e fazem cálculos do escopo delimitado. |
| `v0.5.0` | Agente 3 consolida evidências e gera um relatório de revisão. |
| `v0.6.0` | Interface simples demonstra consulta e análise prévia com dados fictícios. |
| `v0.7.0` | Casos de referência avaliam acertos, erros e limitações. |
| `v1.0.0` | Protótipo e documentação consolidados para apresentação do TCC. |

Cada versão será uma evolução cumulativa, executável a partir de um clone limpo. Tags Git preservarão cada entrega; não serão mantidas cópias do código em pastas separadas para cada versão.

Consulte [o plano detalhado](docs/plano-de-construcao.md) e as instruções de colaboração em [AGENTS.md](AGENTS.md).