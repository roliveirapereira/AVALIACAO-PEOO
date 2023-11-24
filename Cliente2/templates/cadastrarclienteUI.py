import streamlit as st
from views import View
import time

class CadastrarClienteUI:
  def main():
    st.header("Cadastro de Clientes")
    CadastrarClienteUI.inserir()

  def inserir():
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    if st.button("Inserir"):
      View.cliente_inserir(nome, email, fone)
      st.success("Cliente inserido com sucesso")
      time.sleep(2)
      st.rerun()
