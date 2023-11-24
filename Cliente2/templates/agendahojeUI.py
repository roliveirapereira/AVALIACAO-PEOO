import streamlit as st
import pandas as pd
from views import View
import time
import datetime

class agendaHojeUI:
  def main():
    st.header("Agenda de Hoje")
    agendaHojeUI.listar()

  def listar():
    agendas = View.agenda_listar_hoje()
    if len(agendas) == 0:
      st.write("Nenhum horário cadastrado")
    else:
      dic = []
      for obj in agendas: dic.append(obj.to_json())
      df = pd.DataFrame(dic)
      st.dataframe(df)