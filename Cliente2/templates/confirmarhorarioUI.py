import streamlit as st
import pandas as pd
from views import View

class ConfirmarHorarioUI:
  def main():
    st.header("Horários Hoje")
    ConfirmarHorarioUI.confirmar()

  def confirmar():
    agendas = View.agenda_solicitados()
    if len(agendas) == 0:
      st.write("Nenhum horário solicitado")
    else:
      dic = []
      for obj in agendas: dic.append(obj.to_json())
      df = pd.DataFrame(dic)
      st.dataframe(df)
      horario = st.selectbox("Horários solicitados", agendas)
      if st.button("Confirmar"):
          View.agenda_atualizar(horario.get_id(), horario.get_data(), True, horario.get_id_cliente(), horario.get_id_cliente())
          st.success("Horário confirmado")