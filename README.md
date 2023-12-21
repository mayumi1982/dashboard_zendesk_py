# Dashboard de Atendimento com Python

O dashboard que foi apresentado utiliza a biblioteca Streamlit para criar uma interface interativa com gráficos e métricas relacionadas ao atendimento realizado pelo Zendesk, no mês de dezembro/2023.

Vou explicar cada seção do código:
```
import streamlit as st
import plotly.graph_objs as go
```
Importamos o Streamlit para construir o dashboard e a biblioteca Plotly para criar gráficos interativos.

### Definição dos dados:
Definimos os dados fornecidos, como o total de chamados atendidos, atendimentos por agente, tempos de resposta, Net Promoter Score (NPS) e os números de chamados enviados e resolvidos por semana.

### Cálculos:
Calculamos a expectativa por semana dividindo o total de chamados pelo número de semanas (30 dias / 7 dias por semana).

### Título do Dashboard:
```
st.title('Dashboard de Métricas de Atendimento')
```
### Gráficos:

##### - Gráfico de Pizza (Chamados Atendidos por Atendente):
Utiliza a biblioteca Plotly para criar um gráfico de pizza representando a distribuição dos chamados entre os atendentes.

##### - Gráfico de Barras (NPS - Net Promoter Score):
Exibe um gráfico de barras empilhadas para representar o NPS, com barras verdes para avaliação positiva e vermelhas para avaliação negativa.

##### - Gráfico de Barras (Métricas de Tempo de Atendimento):
Mostra um gráfico de barras agrupadas com as métricas de tempo de atendimento, como tempo médio de primeira resposta, tempo médio de resolução de problemas e tempo médio de espera.

##### - Gráfico de Barras (Chamados Enviados e Resolvidos por Semana):
Representa com barras separadas os chamados enviados e resolvidos na mesma semana, mostrando a distribuição dessas métricas ao longo de três semanas.

### Outras Métricas:
Apresenta as métricas de 30 dias, incluindo o total de chamados atendidos e a expectativa de chamados por semana.

[Dashboard de Métricas de Atendimento](https://github.com/mayumi1982/dashboard_zendesk_py/assets/70608757/404604e7-9a36-42d5-bc8a-344cfe267655)

Essas visualizações e métricas ajudam a compreender diferentes aspectos do atendimento ao cliente, desde a distribuição de chamados por agente até o tempo médio de resposta e satisfação geral dos clientes.
