import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Conversor de Extrato", page_icon="📊")

st.title("📊 Conversor Santander -> Modelo")
st.markdown("Faça upload do extrato em **CSV** e baixe a planilha **XLSX** formatada.")

uploaded_file = st.file_uploader("Arraste o extrato do banco aqui", type=["csv"])

if uploaded_file is not None:
    try:
        try:
            df = pd.read_csv(uploaded_file, sep=';', encoding='utf-8', skiprows=2)
        except:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file, sep=';', encoding='latin1', skiprows=2)

        def limpar_moeda(x):
            if isinstance(x, str):
                return float(x.replace('.', '').replace(',', '.'))
            return x

        col_hist = [c for c in df.columns if "ist" in c][0]
        col_doc  = [c for c in df.columns if "Doc" in c][0]
        col_val  = [c for c in df.columns if "Valor" in c][0]
        col_saldo = [c for c in df.columns if "Saldo" in c][0]

        df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y', errors='coerce')
        df = df.dropna(subset=['Data'])
        df = df.sort_values(by='Data', ascending=False)
        
        df['Data_Formatada'] = df['Data'].dt.strftime('%d/%m/%Y')
        df[col_val] = df[col_val].apply(limpar_moeda)
        df[col_saldo] = df[col_saldo].apply(limpar_moeda)

        df_lanara = pd.DataFrame()
        df_lanara['Data'] = df['Data_Formatada']
        df_lanara['Tipo'] = df[col_hist] 
        df_lanara['Histórico'] = ""
        df_lanara['Documento'] = df[col_doc]
        df_lanara['Valor (R$)'] = df[col_val]
        df_lanara['Saldo'] = df[col_saldo]
        df_lanara['Categoria'] = ""
        df_lanara['Obs'] = ""

        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            df_lanara.to_excel(writer, index=False, sheet_name='Extrato')
            
            workbook = writer.book
            worksheet = writer.sheets['Extrato']
            
            formato_moeda = workbook.add_format({'num_format': 'R$ #,##0.00'})
            
            worksheet.set_column('A:A', 12)
            worksheet.set_column('B:B', 30)
            worksheet.set_column('C:C', 20)
            worksheet.set_column('D:D', 15)
            worksheet.set_column('E:F', 18, formato_moeda)
            worksheet.set_column('G:H', 20)
            
        buffer.seek(0)

        st.success("✅ Arquivo processado com sucesso!")
        st.download_button(
            label="📥 Baixar Planilha Formatada",
            data=buffer,
            file_name="Extrato_Planilha_Pronto.xlsx",
            mime="application/vnd.ms-excel"
        )

    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")