#importando bibliotecas
import pandas as pd
import streamlit as st
import plotly.express as px

# Importando os dados do sensor com encoding latin1
dados_sensor = pd.read_csv('sensor_data.csv', encoding='latin1')

# Garante que a coluna 'Data e Hora' está como datetime
if not pd.api.types.is_datetime64_any_dtype(dados_sensor['Data e Hora']):
    dados_sensor['Data e Hora'] = pd.to_datetime(dados_sensor['Data e Hora'], errors='coerce')

st.title('Mapaemaento de agrimenssura')
# Filtro de datas na sidebar (multiseleção, estilo calendário)
datas_unicas = sorted(dados_sensor['Data e Hora'].dt.date.unique())
datas_selecionadas = st.sidebar.multiselect(
    'Selecione as datas:',
    options=datas_unicas,
    default=datas_unicas[:1],
    format_func=lambda x: x.strftime('%d/%m/%Y')
)

# Filtra o DataFrame pelas datas selecionadas
if datas_selecionadas:
    dados_filtrados = dados_sensor[dados_sensor['Data e Hora'].dt.date.isin(datas_selecionadas)]
else:
    dados_filtrados = dados_sensor.copy()

tabs = st.tabs(["pH", "Temperatura", "Nitrogênio", "Fósforo", "Potássio"])

with tabs[0]:
    # Gráfico estilo grade (scatter com cor pelo pH)
    fig_ph = px.scatter(
        dados_filtrados,
        x='Longitude',
        y='Latitude',
        color='pH',
        color_continuous_scale='Viridis',
        labels={'Longitude': 'Longitude', 'Latitude': 'Latitude', 'pH': 'pH'},
        title='Distribuição de pH por Localização',
        hover_data=['pH', 'Data e Hora']
    )
    fig_ph.update_traces(marker=dict(size=8))
    st.plotly_chart(fig_ph, use_container_width=True)
    # Mapa de calor para pH
    fig_ph_map = px.density_mapbox(
        dados_filtrados,
        lat='Latitude',
        lon='Longitude',
        z='pH',
        radius=20,
        center=dict(lat=dados_filtrados['Latitude'].mean(), lon=dados_filtrados['Longitude'].mean()),
        zoom=10,
        mapbox_style="open-street-map",
        color_continuous_scale='Viridis',
        title='Mapa de Calor de pH'
    )
    st.plotly_chart(fig_ph_map, use_container_width=True)

with tabs[1]:
    # Gráfico estilo grade (scatter com cor pela Temperatura)
    fig_temp = px.scatter(
        dados_filtrados,
        x='Longitude',
        y='Latitude',
        color='Temperatura',
        color_continuous_scale='RdYlBu',
        labels={'Longitude': 'Longitude', 'Latitude': 'Latitude', 'Temperatura': 'Temperatura'},
        title='Distribuição de Temperatura por Localização',
        hover_data=['Temperatura', 'Data e Hora']
    )
    fig_temp.update_traces(marker=dict(size=8))
    st.plotly_chart(fig_temp, use_container_width=True)
    # Mapa de calor para Temperatura
    fig_temp_map = px.density_mapbox(
        dados_filtrados,
        lat='Latitude',
        lon='Longitude',
        z='Temperatura',
        radius=20,
        center=dict(lat=dados_filtrados['Latitude'].mean(), lon=dados_filtrados['Longitude'].mean()),
        zoom=10,
        mapbox_style="open-street-map",
        color_continuous_scale='RdYlBu',
        title='Mapa de Calor de Temperatura'
    )
    st.plotly_chart(fig_temp_map, use_container_width=True)

with tabs[2]:
    # Gráfico para Nitrogênio
    fig_n = px.scatter(
        dados_filtrados,
        x='Longitude',
        y='Latitude',
        color='Nitrogênio',
        color_continuous_scale='Greens',
        labels={'Longitude': 'Longitude', 'Latitude': 'Latitude', 'Nitrogênio': 'Nitrogênio'},
        title='Distribuição de Nitrogênio por Localização',
        hover_data=['Nitrogênio', 'Data e Hora']
    )
    fig_n.update_traces(marker=dict(size=8))
    st.plotly_chart(fig_n, use_container_width=True)
    # Mapa de calor para Nitrogênio
    fig_n_map = px.density_mapbox(
        dados_filtrados,
        lat='Latitude',
        lon='Longitude',
        z='Nitrogênio',
        radius=20,
        center=dict(lat=dados_filtrados['Latitude'].mean(), lon=dados_filtrados['Longitude'].mean()),
        zoom=10,
        mapbox_style="open-street-map",
        color_continuous_scale='Greens',
        title='Mapa de Calor de Nitrogênio'
    )
    st.plotly_chart(fig_n_map, use_container_width=True)

with tabs[3]:
    # Gráfico para Fósforo
    fig_p = px.scatter(
        dados_filtrados,
        x='Longitude',
        y='Latitude',
        color='Fósforo',
        color_continuous_scale='Purples',
        labels={'Longitude': 'Longitude', 'Latitude': 'Latitude', 'Fósforo': 'Fósforo'},
        title='Distribuição de Fósforo por Localização',
        hover_data=['Fósforo', 'Data e Hora']
    )
    fig_p.update_traces(marker=dict(size=8))
    st.plotly_chart(fig_p, use_container_width=True)
    # Mapa de calor para Fósforo
    fig_p_map = px.density_mapbox(
        dados_filtrados,
        lat='Latitude',
        lon='Longitude',
        z='Fósforo',
        radius=20,
        center=dict(lat=dados_filtrados['Latitude'].mean(), lon=dados_filtrados['Longitude'].mean()),
        zoom=10,
        mapbox_style="open-street-map",
        color_continuous_scale='Purples',
        title='Mapa de Calor de Fósforo'
    )
    st.plotly_chart(fig_p_map, use_container_width=True)

with tabs[4]:
    # Gráfico para Potássio
    fig_k = px.scatter(
        dados_filtrados,
        x='Longitude',
        y='Latitude',
        color='Potássio',
        color_continuous_scale='Oranges',
        labels={'Longitude': 'Longitude', 'Latitude': 'Latitude', 'Potássio': 'Potássio'},
        title='Distribuição de Potássio por Localização',
        hover_data=['Potássio', 'Data e Hora']
    )
    fig_k.update_traces(marker=dict(size=8))
    st.plotly_chart(fig_k, use_container_width=True)
    # Mapa de calor para Potássio
    fig_k_map = px.density_mapbox(
        dados_filtrados,
        lat='Latitude',
        lon='Longitude',
        z='Potássio',
        radius=20,
        center=dict(lat=dados_filtrados['Latitude'].mean(), lon=dados_filtrados['Longitude'].mean()),
        zoom=10,
        mapbox_style="open-street-map",
        color_continuous_scale='Oranges',
        title='Mapa de Calor de Potássio'
    )
    st.plotly_chart(fig_k_map, use_container_width=True)

