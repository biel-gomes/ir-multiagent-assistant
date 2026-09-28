from crews import responder_gerente_tcc

pergunta = """
Estou começando o desenvolvimento do meu TCC.

O projeto será um sistema multiagentes utilizando CrewAI
para auxiliar contribuintes no processo de declaração
do Imposto de Renda.

Organize os primeiros passos do desenvolvimento.
"""

resultado = responder_gerente_tcc(pergunta, historico=[])

print("\nRESULTADO:\n")
print(resultado)
