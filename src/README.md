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

# Evidências de execução.

<img width="971" height="572" alt="Captura de ecrã 2026-04-04 164218" src="https://github.com/user-attachments/assets/cec04b15-f7b2-48ab-9a8d-6171b9867c40" />
<img width="1070" height="726" alt="Captura de ecrã 2026-04-04 164312" src="https://github.com/user-attachments/assets/56d3d769-05e1-49f7-ab87-36dbfe6ff4f7" />
<img width="1124" height="757" alt="Captura de ecrã 2026-04-04 164156" src="https://github.com/user-attachments/assets/7506732b-dd55-42db-a99c-f54c97b32168" />


https://github.com/user-attachments/assets/abe7b954-60ff-4dfa-9df3-5655518757bc


streamlit run app.py
```
