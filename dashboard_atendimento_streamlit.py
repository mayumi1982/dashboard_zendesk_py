import streamlit as st
import plotly.graph_objs as go

# Dados fornecidos
total_chamados = 208
atendimentos = {'Danielle': 123, 'Tatiane': 82, 'Giovanni': 3}
tempo_primeira_resposta = 1
tempo_resolucao_problema = 4.5
tempo_espera = 2.3
nps_bom = 138
nps_ruim = 1

# Dados por semana
chamados_semana = [97, 69, 49]
resolvidos_semana = [89, 70, 49]

# Período de 30 dias
dias_periodo = 30

# Cálculo da expectativa por semana
expectativa_semana = total_chamados / (dias_periodo / 7)

# Título do Dashboard
st.title('Dashboard de Métricas de Atendimento')

# Gráfico de pizza para representar a divisão dos chamados por atendente
fig_atendentes = go.Figure(data=[go.Pie(labels=list(atendimentos.keys()), values=list(atendimentos.values()))])
fig_atendentes.update_layout(title='Chamados Atendidos por Atendente')
st.plotly_chart(fig_atendentes)

# Gráfico de barras para NPS (Net Promoter Score)
fig_nps = go.Figure(data=[
    go.Bar(name='Bom', x=['NPS'], y=[nps_bom], marker=dict(color='green')),
    go.Bar(name='Ruim', x=['NPS'], y=[nps_ruim], marker=dict(color='red'))
])
fig_nps.update_layout(barmode='stack', title='Net Promoter Score (NPS)')
st.plotly_chart(fig_nps)

# Gráfico de barras para métricas de tempo de atendimento
fig_tempo_atendimento = go.Figure(data=[
    go.Bar(name='Tempo de Primeira Resposta (min)', x=['Tempo de Primeira Resposta'], y=[tempo_primeira_resposta]),
    go.Bar(name='Tempo de Resolução de Problema (horas)', x=['Tempo de Resolução de Problema'], y=[tempo_resolucao_problema]),
    go.Bar(name='Tempo de Espera (horas)', x=['Tempo de Espera'], y=[tempo_espera])
])
fig_tempo_atendimento.update_layout(barmode='group', title='Métricas de Tempo de Atendimento')
st.plotly_chart(fig_tempo_atendimento)

# Gráfico de barras para chamados enviados e resolvidos por semana
fig_semanas = go.Figure(data=[
    go.Bar(name='Chamados Enviados', x=['Semana 1', 'Semana 2', 'Semana 3'], y=chamados_semana),
    go.Bar(name='Resolvidos na Mesma Semana', x=['Semana 1', 'Semana 2', 'Semana 3'], y=resolvidos_semana)
])
fig_semanas.update_layout(barmode='group', title='Chamados Enviados e Resolvidos por Semana')
st.plotly_chart(fig_semanas)

# Outras métricas
st.subheader('Métricas de 30 dias')
st.write(f'Total de Chamados Atendidos: {total_chamados}')
st.write(f'Expectativa por Semana: {expectativa_semana:.2f}')


