import streamlit as st
from nexo import pergunta_ao_nexo

st.set_page_config(page_title="Nexo", page_icon="🤖💰")

# Cabeçalho com emoji e texto centralizado no topo
st.markdown("""
    <div style="text-align: center; margin-top: 20px; margin-bottom: 20px;">
        <div style="font-size: 120px; color: #1E90FF;">🤖</div>
        <div style="font-size: 24px; color: #1E90FF; font-weight: 600;">seu robozinho financeiro!</div>
    </div>
""", unsafe_allow_html=True)

# Caixa para entrada da pergunta, já logo após o topo
pergunta = st.text_input("💬 Manda a tua pergunta para o Nexo:", key="input_pergunta")

# Botões lado a lado logo abaixo do input
col1, col2 = st.columns([1, 1])
with col1:
    enviar = st.button("🚀 Enviar", key="botao_enviar")
with col2:
    nova_conversa = st.button("🔄 Nova conversa", key="botao_nova_conversa")

# Lógica do envio da pergunta
if enviar and pergunta.strip():
    with st.spinner("Nexo está digitando..."):
        resposta, st.session_state.historico_chat = pergunta_ao_nexo(pergunta, st.session_state.get("historico_chat"))
        st.session_state.pergunta_enviada = pergunta
        st.session_state.resposta_nexo = resposta

# Lógica para nova conversa (reseta o histórico)
if nova_conversa:
    st.session_state.historico_chat = None
    st.session_state.pergunta_enviada = None
    st.session_state.resposta_nexo = None

# Exibe o diálogo se existir
if st.session_state.get("resposta_nexo"):
    st.markdown("---")
    st.markdown(f"**👤 Você:** {st.session_state.pergunta_enviada}")
    st.markdown(f"**🤖 Nexo:** {st.session_state.resposta_nexo}")
