from datetime import datetime
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tabla Interactiva", layout="wide")

st.title("📝 Generación de Informe Reportes Central Ñuñoa 2026")

# Título y botones en una fila
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("Inicio", key="nav_home",width='stretch'):
        st.switch_page("app.py")
        
with col2:
    if st.button("Mapa Interactivo", key="nav_mapa", width='stretch'):
        st.switch_page("pages/1_Mapa_Interactivo.py")

with col3:
    if st.button("Dashboard", key="nav_dash", width='stretch'):
        st.switch_page("pages/2_Dashboard.py")

with col4:
    if st.button("Tabla Interactiva", key="nav_tabla", width='stretch'):
        st.switch_page("pages/3_Tabla_Interactiva.py")
with col5:
    if st.button("Exportar Reportes", key="nav_report", width='stretch'):
        st.switch_page("pages/4_Exportar_Reportes.py")
st.markdown("---")

st.subheader("Selección de Filtros")