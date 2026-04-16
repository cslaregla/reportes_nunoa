import streamlit as st

## Configuración inicial aplicación ##
## El logo es el archivo logo.png ubicado en la misma carpeta que este archivo ##
## En caso de querer cambiar el logo, ubicar en esta carpeta un archivo png con el mismo nombre y borrar el antiguo ##
st.set_page_config(
    page_title="Inicio",
    page_icon="./logo.png",
    initial_sidebar_state="collapsed",
    layout="wide"
)
st.logo("./logo.png",size='large',icon_image="./logo.png")
st.title("ℹ️ Reportes Procedimientos Central Ñuñoa 2026")

## Validación por seguridad ##
from auth import check_auth
if not check_auth():
    st.stop()

## Título y botones en una fila ##
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    if st.button("Inicio", key="nav_home", width='stretch'):
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

with col6:
    if st.button("Gráficas Comparativas", key='nav_comp', width='stretch'):
        st.switch_page("pages/5_Graficas_Comparativas.py")

## Descripción general de la aplicación ##
st.markdown("---")
st.header("Bienvenido, esta herramienta permite:")
st.write("""
- 🗺️ Visualizar reportes georeferenciados en un mapa de calor
- 📈 Analizar datos a través de gráficas y métricas
- 🗃️ Búsquedas personalizadas por filtros en tabla de datos
- 📝 Generar informes estandarizados y automatizados
- ⚖️ Comparar tipos de procedimientos por período de tiempo

Selecciona una opción en el menú para comenzar.
""")