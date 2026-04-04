import json
import pandas as pd
from groq import Groq

# ========== CARREGAR DADOS (mantido original) ==========
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ========== MONTAR CONTEXTO ==========
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ========== SYSTEM PROMPT ==========
SYSTEM_PROMPT = """
Você é **Nexo**, um agente financeiro jovem, claro e inteligente. 
Seu papel é ajudar pessoas entre 16 e 24 anos a entender melhor o próprio dinheiro, 
corrigir hábitos ruins, criar consciência financeira e desenvolver práticas saudáveis 
de organização e poupança — sempre de forma simples, acessível e sem recomendações 
de investimentos de risco.

## COMO O NEXO PENSA E AGE
- Sempre se apresentar, dizer seu nome (Nexo).
- Fala de forma leve, direta e jovem.
- Explica conceitos financeiros de maneira simples, sem jargões desnecessários.
- Ajuda o usuário a entender o *porquê* das coisas, não só o *como*.
- Nunca julga; orienta com clareza e empatia.
- Incentiva hábitos saudáveis e decisões conscientes.

## REGRAS
1. Baseie todas as respostas exclusivamente nos dados fornecidos no contexto.
2. Não invente números, produtos, taxas ou informações financeiras.
3. Não recomende investimentos de risco (ações, FIIs, criptomoedas, derivativos etc.).
4. Se não souber algo, admita com naturalidade e ofereça caminhos alternativos.
5. Priorize educação financeira, não aconselhamento financeiro profissional.
6. Evite termos técnicos complexos; prefira explicações simples, práticas e curtas.
7. Mantenha sempre o tom característico do Nexo: claro, jovem, racional e amigável.
"""

# ========== CONFIGURAÇÃO GROQ ==========
GROQ_API_KEY = "DIGITE_SUA_CHAVE_AQUI"
client = Groq(api_key=GROQ_API_KEY)

def pergunta_ao_nexo(pergunta_usuario: str, historico_chat: list = None) -> tuple[str, list]:
    """
    Recebe pergunta do usuário e retorna resposta do Nexo + histórico atualizado.
    Mantém contexto da conversa para próximas interações.
    """
    if historico_chat is None:
        historico_chat = [
            {"role": "system", "content": SYSTEM_PROMPT + "\n\nCONTEXTO:\n" + contexto}
        ]
    
    # Adiciona pergunta do usuário ao histórico
    historico_chat.append({"role": "user", "content": pergunta_usuario})

    resposta_final = ""
    stream = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=historico_chat,
        stream=True
    )

    for chunk in stream:
        delta_obj = chunk.choices[0].delta
        token = getattr(delta_obj, "content", None)
        if token:
            resposta_final += token

    # Adiciona resposta do Nexo ao histórico
    historico_chat.append({"role": "assistant", "content": resposta_final})

    return resposta_final, historico_chat

# ========== integração com Streamlit ==========
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

    #pode executar o steamlit run src/app.py direto no terminal do codigo!
