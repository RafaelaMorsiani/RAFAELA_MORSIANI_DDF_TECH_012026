import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard MK", layout="wide")

try:
    # Carregando os dados que você já gerou
    df = pd.read_csv('ecommerce_products_enriched.csv')

    st.title("📊 Dashboard MK E-commerce")

    # KPIs
    c1, c2 = st.columns(2)
    c1.metric("Faturamento Total", f"R$ {df['price'].sum():,.2f}")
    c2.metric("Ticket Médio", f"R$ {df['price'].mean():.2f}")

    # Gráfico simples de Categorias
    st.subheader("Vendas por Categoria")
    fig = px.bar(df.groupby('category')['price'].sum().reset_index(), x='category', y='price')
    st.plotly_chart(fig, use_container_width=True)

    # Tabela com a IA
    st.subheader("🔍 Atributos Extraídos por IA")
    st.dataframe(df[['title', 'material', 'tecnologia']])

except Exception as e:
    st.error(f"Erro: {e}. Certifique-se que o arquivo 'ecommerce_products_enriched.csv' existe.")
