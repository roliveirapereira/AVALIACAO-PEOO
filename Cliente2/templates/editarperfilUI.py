import streamlit as st
from views import View
import time

class EditarPerfilUI:
    def main():
       st.header("Editar Perfil")
       EditarPerfilUI.atualizar()
       
    def atualizar():
       for cliente in View.cliente_listar():
         if cliente.get_id() == st.session_state["cliente_id"]:
           c = cliente
       nome = st.text_input("Informe o novo nome", c.get_nome())
       email = st.text_input("Informe o novo e-mail", c.get_email())
       fone = st.text_input("Informe o novo fone", c.get_fone())
       senha = st.text_input("Informe a nova senha", c.get_senha())
       if st.button("Atualizar"):
          id = c.get_id()
          View.cliente_atualizar(id, nome, email, fone, senha)
          st.success("Cliente atualizado com sucesso")
          time.sleep(2)
          st.rerun()