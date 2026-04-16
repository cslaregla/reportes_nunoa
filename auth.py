import streamlit as st

## Implementación de una verificación simple para acceder a la aplicación ##

def check_auth():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if st.session_state.authenticated:
        return True

    password = st.text_input("Para continuar ingrese la contraseña:", type="password")

    if st.button("Iniciar sesión"):
        if password == st.secrets["APP_PASSWORD"]:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Contraseña incorrecta")

    return False