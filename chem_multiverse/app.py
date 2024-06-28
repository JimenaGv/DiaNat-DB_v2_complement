import streamlit as st
import plotly.express as px
import pandas as pd

def main():
    # Cargar los datos que ya tienen los resultados de t-SNE
    df_tsne1 = pd.read_csv('https://raw.githubusercontent.com/DIFACQUIM/DiaNat-DB_v2/main/data_sets/tsne_ecfp4.csv')
    df_tsne2 = pd.read_csv('https://raw.githubusercontent.com/DIFACQUIM/DiaNat-DB_v2/main/data_sets/tsne_props.csv')

    # Define el mapa de colores usando códigos HTML
    color_discrete_map = {
        'FDA': '#FEC107',
        'UNPD-A': '#4FBB53',
        'ChEMBL': '#EA1E63',
        'DiaNat-DB': '#2196F3',
        'COCONUT':'#c3c6c9'
    }

    # Crear la aplicación de Streamlit
    st.title('Chemical multiverse visualization')

    # Gráfico 1
    st.subheader('ECFP4 (1024-bits)')
    fig1 = px.scatter(
        df_tsne1,
        x='t-SNE Dimension 1',
        y='t-SNE Dimension 2',
        color='database',
        title='ECFP4',
        color_discrete_map=color_discrete_map,
        hover_data={
            'id': True,         # Mostrar ID del compuesto
            'database': True,   # Mostrar Database
            't-SNE Dimension 1': False,     # Ocultar TSNE1
            't-SNE Dimension 2': False      # Ocultar TSNE2
        },
        labels={
            'database': 'Database ',
            'id': 'Compound ID '
        },
        width=800,  # Ajustar el ancho de la gráfica
        height=800  # Ajustar la altura de la gráfica
    )
    st.plotly_chart(fig1)

    # Texto como pie de figura
    st.markdown("Extended-connectivity fingerprint with diameter 4 was used as molecular representation, and t-SNE was employed for dimensionality reduction.")
    
    # Gráfico 2
    st.subheader("Properties related to Lipinski and Veber's rules")
    fig2 = px.scatter(
        df_tsne2,
        x='t-SNE Dimension 1',
        y='t-SNE Dimension 2',
        color='database',
        title="Properties",
        color_discrete_map=color_discrete_map,
        hover_data={
            'id': True,         # Mostrar ID del compuesto
            'database': True,   # Mostrar Database
            't-SNE Dimension 1': False,     # Ocultar TSNE1
            't-SNE Dimension 2': False      # Ocultar TSNE2
        },
        labels={
            'database': 'Database ',
            'id': 'Compound ID '
        },
        width=800,  # Ajustar el ancho de la gráfica
        height=800  # Ajustar la altura de la gráfica
    )
    st.plotly_chart(fig2)

    # Texto como pie de figura
    st.markdown("Properties related to Lipinski and Veber's rules (MW, HBA, HBD, logP, TPSA and nRotBonds) were used as molecular descriptors, and t-SNE was employed for dimensionality reduction.")
    

if __name__ == '__main__':
    main()
