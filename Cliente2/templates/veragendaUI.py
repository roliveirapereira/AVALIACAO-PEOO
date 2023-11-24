import streamlit as st
import pandas as pd
from views import View

class VerAgendaUI:
  def main():
    st.header("Meus agendamentos")
    VerAgendaUI.listar()

  def listar():
    cliente = View.cliente_listar_id(st.session_state["cliente_id"])
    agendas = View.agenda_listarcliente(cliente)
    inicio = st.text_input("Informe a data inicial no formato DD/MM/AAAA")
    final = st.text_input("Informe a data final no formato DD/MM/AAAA")
    if st.button("Ver agenda"):
      if len(agendas) == 0:
        st.write("Você não possui nenhum agendamento")
      else:
        dic = []
        for obj in agendas: 
          if View.agenda_periodo(obj, inicio, final): dic.append(obj.to_json())
        df = pd.DataFrame(dic)
        st.dataframe(df)