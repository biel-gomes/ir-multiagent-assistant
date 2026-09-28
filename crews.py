from crewai import Crew, Task

from agentes import (
    criar_analista_situacao,
    criar_gerente_tcc,
    criar_guia_declaracao,
    criar_orientador_documentos,
)
from llm import get_llm

def _historico_texto(historico: list[dict[str, str]]) -> str:
    if not historico:
        return "(nenhuma conversa anterior)"
    linhas = []
    for mensagem in historico[-12:]:
        papel = "Usuário" if mensagem["role"] == "user" else "Assistente"
        linhas.append(f"{papel}: {mensagem['content']}")
    return "\n".join(linhas)


def responder_gerente_tcc(pergunta: str, historico: list[dict[str, str]]) -> str:
    llm = get_llm()
    gerente = criar_gerente_tcc(llm)

    tarefa = Task(
        description=f"""
        Conversa anterior:
        {_historico_texto(historico)}

        Nova dúvida sobre o desenvolvimento do TCC:
        {pergunta}

        Evite repetir o que já foi dito. Foque em decisões e próximos passos.
        """,
        expected_output=(
            "Uma resposta objetiva e prática, priorizando próximos passos."
        ),
        agent=gerente,
    )

    crew = Crew(agents=[gerente], tasks=[tarefa], verbose=False)
    return str(crew.kickoff())


def responder_ir(pergunta: str, historico: list[dict[str, str]]) -> str:
    llm = get_llm()
    analista = criar_analista_situacao(llm)
    orientador = criar_orientador_documentos(llm)
    guia = criar_guia_declaracao(llm)

    contexto = _historico_texto(historico)

    analisar = Task(
        description=f"""
        Conversa anterior:
        {contexto}

        Relato ou pergunta atual do contribuinte:
        {pergunta}

        Resuma a situação fiscal possível, liste o que está claro
        e o que ainda precisa ser perguntado.
        """,
        expected_output=(
            "Um resumo curto da situação, lacunas de informação "
            "e hipóteses razoáveis sem inventar dados."
        ),
        agent=analista,
    )

    documentos = Task(
        description="""
        Com base na análise da situação, indique os documentos
        mais relevantes para este contribuinte reunir.
        """,
        expected_output="Uma lista objetiva de documentos, só os pertinentes.",
        agent=orientador,
        context=[analisar],
    )

    orientar = Task(
        description="""
        Una a análise e a lista de documentos em uma resposta final
        para o contribuinte.

        Estrutura obrigatória:
        1. O que ficou claro
        2. O que ainda falta informar
        3. Documentos sugeridos
        4. Próximo passo prático

        Inclua um aviso curto de que isso não substitui a Receita Federal
        nem um contador.
        """,
        expected_output="Resposta clara, em português, com as quatro seções.",
        agent=guia,
        context=[analisar, documentos],
    )

    crew = Crew(
        agents=[analista, orientador, guia],
        tasks=[analisar, documentos, orientar],
        verbose=False,
    )
    return str(crew.kickoff())
