import streamlit as st

from llm import get_api_key
from crews import responder_gerente_tcc, responder_ir

st.set_page_config(
    page_title="Assistente de TCC — IR",
    page_icon="🧾",
    layout="centered",
)

MODO_IR = "Assistente de Imposto de Renda"
MODO_TCC = "Gerente do TCC"

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []
if "modo" not in st.session_state:
    st.session_state.modo = MODO_IR


def limpar_chat():
    st.session_state.mensagens = []


st.title("Assistente virtual para o TCC")
st.caption(
    "Sistema multiagentes com CrewAI para orientar a declaração do IR "
    "e organizar o desenvolvimento do trabalho."
)

with st.sidebar:
    st.header("Configuração")
    modo = st.radio(
        "Modo",
        [MODO_IR, MODO_TCC],
        index=0 if st.session_state.modo == MODO_IR else 1,
    )
    if modo != st.session_state.modo:
        st.session_state.modo = modo
        st.session_state.mensagens = []
        st.rerun()

    st.button("Limpar conversa", on_click=limpar_chat)
    st.markdown(
        "O assistente de IR **não substitui** a Receita Federal nem um contador."
    )

if not get_api_key():
    st.error(
        "GEMINI_API_KEY não encontrada. Coloque a chave no arquivo `.env` "
        "na pasta do projeto."
    )
    st.stop()

for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

placeholder = (
    "Descreva sua situação ou tire uma dúvida sobre a declaração"
    if st.session_state.modo == MODO_IR
    else "Pergunte sobre o desenvolvimento do TCC"
)

pergunta = st.chat_input(placeholder)

if pergunta:
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.write(pergunta)

    historico = st.session_state.mensagens[:-1]
    with st.chat_message("assistant"):
        with st.spinner("Os agentes estão analisando..."):
            try:
                if st.session_state.modo == MODO_IR:
                    resposta = responder_ir(pergunta, historico)
                else:
                    resposta = responder_gerente_tcc(pergunta, historico)
            except Exception as erro:
                resposta = f"Não foi possível concluir a resposta: {erro}"
        st.write(resposta)

    st.session_state.mensagens.append({"role": "assistant", "content": resposta})
