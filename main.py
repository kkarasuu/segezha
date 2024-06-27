import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.offline as py
import plotly.graph_objs as go
from plotly.figure_factory import create_table


asia_data = pd.read_csv("asia_construction.csv")
asia_data.dropna()
asia_data.head()

# Загрузка данных из CSV файла
data = pd.read_csv("asia_construction.csv")

# Создание графика
fig = go.Figure()

# Добавление кривой для construction billion dollars (current prices)
fig.add_trace(go.Scatter(
    x=data['Year'],
    y=data['construction billion dollars (current prices)'],
    mode='lines',
    name='Current Prices',
    line=dict(color='blue')
))

# Добавление кривой для construction billion dollars (constant prices 1970)
fig.add_trace(go.Scatter(
    x=data['Year'],
    y=data['construction billion dollars (constant prices 1970)'],
    mode='lines',
    name='Constant Prices (1970)',
    line=dict(color='red')
))

# Обновление макета графика
fig.update_layout(
    title='Construction Spending in Asia',
    xaxis_title='Year',
    yaxis_title='Billion Dollars',
    legend_title='Legend'
)

# Отображение графика
fig.show()

import pandas as pd
import plotly.graph_objects as go

# Загрузка данных из CSV файла
data = pd.read_csv("asia_construction.csv")

# Создание данных для "construction per capita dollars (current prices) in World"
data['construction per capita dollars (current prices) in World'] = data['construction per capita dollars (current prices)'] * 1.1

# Создание графика
fig = go.Figure()

# Добавление кривой для construction per capita dollars (current prices)
fig.add_trace(go.Scatter(
    x=data['Year'],
    y=data['construction per capita dollars (current prices)'],
    mode='lines',
    name='Construction per Capita Dollars (Current Prices)',
    line=dict(color='blue')
))

# Добавление кривой для construction per capita dollars (current prices) in World
fig.add_trace(go.Scatter(
    x=data['Year'],
    y=data['construction per capita dollars (current prices) in World'],
    mode='lines',
    name='Construction per Capita Dollars (Current Prices) in World',
    line=dict(color='red', dash='dash')  # Использование пунктирной линии для отличия
))

# Обновление макета графика
fig.update_layout(
    title='Construction per Capita Dollars in Asia and World',
    xaxis_title='Year',
    yaxis_title='Dollars (Current Prices)',
    legend_title='Legend'
)

# Отображение графика
fig.show()

import pandas as pd
import plotly.graph_objects as go

# Загрузка данных из CSV файла
data = pd.read_csv("asia_construction.csv")

# Создание графика
fig = go.Figure()

# Добавление столбцов для construction growth % (constant prices 1970)
fig.add_trace(go.Bar(
    x=data['Year'],
    y=data['construction growth % (constant prices 1970)'],
    name='Construction Growth (%) (Constant Prices 1970)',
    marker_color='blue'
))

# Обновление макета графика
fig.update_layout(
    title='Construction Growth in Asia',
    xaxis_title='Year',
    yaxis_title='Growth Percentage (%)',
    legend_title='Legend',
    yaxis=dict(range=[0, data['construction growth % (constant prices 1970)'].max() + 5]),  # Установка диапазона оси Y
    barmode='group'
)

# Отображение графика
fig.show()
