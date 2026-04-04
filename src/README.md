# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
dio-lab-bia-do-futuro-main/ src
├── nexo.py              # Código da lógica do agente Nexo (função pergunta_ao_nexo, carregamento de dados, configuração Groq)
├── app.py               # Aplicação Streamlit que importa a função de nexo.py e monta a interface interativa
├── data/                # Pasta com os arquivos JSON e CSV usados pelo nexo.py
│   ├── perfil_investidor.json
│   ├── transacoes.csv
│   ├── historico_atendimento.csv
│   └── produtos_financeiros.json
├── requirements.txt     # Dependências Python do projeto (ex: streamlit, groq, pandas)

---
```

## Exemplo de requirements.txt

```
streamlit==1.22.0
groq==0.6.5
pandas==2.0.3
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação Streamlit
streamlit run app.py

# Rodar a aplicação
streamlit run app.py
```
