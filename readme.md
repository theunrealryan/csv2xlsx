# 📊 Conversor de Extrato Bancário (CSV para XLSX)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://converter-extrato.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-150458.svg)](https://pandas.pydata.org/)

Um micro-SaaS open-source desenvolvido para automatizar a limpeza, formatação e conversão de extratos bancários (formato CSV) para o padrão de planilhas contábeis (XLSX).

## 🚀 O Problema

A conciliação bancária manual exige formatação repetitiva: exclusão de cabeçalhos inúteis, conversão de tipagem de dados, ordenação cronológica invertida e padronização de moedas. Este projeto elimina esse trabalho manual, transformando um CSV bruto do banco em um Excel pronto para importação no sistema final do cliente em segundos.

## ✨ Funcionalidades

- **Upload Drag-and-Drop:** Interface limpa e intuitiva construída com Streamlit.
- **Data Cleaning Dinâmico:** Ignora automaticamente cabeçalhos e rodapés gerados pelo banco.
- **Conversão de Tipos:** Tratamento robusto para formatos de moeda e datas padrão Brasil.
- **Ordenação Inteligente:** Coloca as transações mais recentes no topo.
- **Exportação Nativa Excel:** Formatação automática de largura de colunas e máscaras contábeis.

## 💻 Demonstração

Você pode testar a aplicação diretamente no navegador:
👉 **[Acessar a Ferramenta Online](https://converter-extrato.streamlit.app/)**

![Demonstração do App](assets/demo.png)

## 🛠️ Como rodar localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/theunrealryan/csv2xlsx.git](https://github.com/theunrealryan/csv2xlsx.git)
   cd csv2xlsx

    Crie e ative um ambiente virtual:
    Bash

    python -m venv venv
    source venv/bin/activate

    Instale as dependências:
    Bash

    pip install -r requirements.txt

    Inicie a aplicação:
    Bash

    streamlit run app.py

## 🏗️ Arquitetura e Decisões Técnicas

O projeto adota uma arquitetura *stateless* baseada em processamento volátil, priorizando a segurança estrutural no manuseio de dados financeiros.

* **Frontend:** Interface reativa construída com **Streamlit**, garantindo renderização *server-side* ágil e navegação fluida.
* **Pipeline ETL (*In-Memory*):** Orquestrado com **Pandas** e `io.BytesIO`. Todo o processamento ocorre na memória RAM do container. A tolerância zero à persistência em disco assegura o isolamento e a privacidade total dos dados bancários.
* **Camada de Exportação:** Motor **XlsxWriter** integrado de forma nativa ao Pandas, responsável por gerar o binário `.xlsx` dinamicamente, injetando metadados e formatação contábil em tempo de execução.
* **Infraestrutura Cloud:** Hospedado no **Streamlit Community Cloud** utilizando *containers* efêmeros. O ambiente possui integração contínua (CI) acoplada ao GitHub e gestão inteligente de recursos via *Scale-to-Zero* (hibernação automática sem tráfego).

📝 Licença

Este projeto é open-source e está licenciado sob a MIT License.
