import streamlit as st
import pandas as pd
from views import View

class AgendarHorarioUI:
  def main():
    st.header("Agendar horário ")
    AgendarHorarioUI.agendar()

  def agendar():
    horarios = View.agenda_listar_semana()
    if len(horarios) == 0:
      st.write("Nenhum horario disponível nesta semana")
    else:  
      dic = []
      for obj in horarios:
        if not obj.get_id_cliente():
          dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)
      horario = st.selectbox("Escolha um horário", horarios)
      servico = st.selectbox("Escolha um serviço", View.servico_listar())
      if st.button("Agendar"):
          id = st.session_state["cliente_id"]
          View.agenda_cliente(id, horario, servico)
          st.success("Horário agendado com sucesso")

