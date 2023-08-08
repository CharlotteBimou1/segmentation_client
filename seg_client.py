import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

logo_image = "pplink.png"  # Replace with the path to your logo image
st.image(logo_image, width=150)

# Perform query.
# Utiliser la balise HTML <div> avec le style CSS pour justifier le texte
st.header('Segmentation de la clientèle par K-Means (Algorithme de Machine Learning non supervisé)')
st.write("**Objectif de l'application** : permettre aux équipes opérationnelles et techniques "
         "de diviser leur base de clients, tant les clients existants que les nouveaux, afin de leur "
         "offrir de nouvelles prestations et d'entreprendre des efforts de prospection auprès de nouveaux "
         "clients potentiels.")
st.write('**Source des données utilisées**: https://archive.ics.uci.edu/dataset/352/online+retail')
st.write('**Informations complémentaires des données**:')
st.write('Ensemble de données transnationales qui contient toutes les transactions effectuées entre le '
         '01/12/2010 et le 09/12/2011 pour un commerce de détail en ligne non-magasin basé au Royaume-Uni '
         'et enregistré. De nombreux clients de cette entreprise sont des grossistes.')
st.write('**Affichage** : Échantillon de données en grappes(groupe) montrant la récurrence, la fréquence et les attributs monétaires de chaque client')

@st.cache_data
def get_data():
    df = pd.read_csv("RFM_Clusters.csv")
    df["Cluster"] = df["Cluster"].astype(str)
    return df

def main():
    # Create two columns layout
    col1, col2 = st.columns([1, 2])

    # Move the dataset to the left column
    df_pd = get_data()
    col1.dataframe(df_pd)

    # Move the graphs to the right column
    col2.subheader('Fréquence des clients en fonction de leurs récences sur le site e-commerce')
    fig = px.scatter(
        df_pd,
        x="Frequency",
        y="RECENCY",
        color="Cluster",
        opacity=0.5
    )
    col2.plotly_chart(fig, theme="streamlit", use_container_width=True)

    col2.subheader('Fréquence des clients en fonction de leurs dépenses monétaire')
    fig = px.scatter(
        df_pd,
        x="Frequency",
        y="Monetary",
        color="Cluster",
        opacity=0.5
    )
    col2.plotly_chart(fig, theme="streamlit", use_container_width=True)

    col2.subheader('Récense des clients sur le site e-commerce en fonction de leurs dépenses')
    fig = px.scatter(
        df_pd,
        x="RECENCY",
        y="Monetary",
        color="Cluster",
        opacity=0.5
    )
    col2.plotly_chart(fig, theme="streamlit", use_container_width=True)

    # Move the markdown text to the left column
    col1.markdown("**:blue[Cluster 3]** sont des clients loyalistes. Ils dépensent généralement plus d'argent et plus fréquemment")
    col1.markdown("**:orange[Cluster 1]** sont des clients en croissance. Ils dépensent moins d'argent et moins fréquemment, mais ils ont dépensé au cours des 5 derniers mois.")
    col1.markdown("**:pink[Cluster 2]** sont vos clients en perte de vitesse. Ils dépensent moins d'argent et moins fréquemment, et ils ont dépensé au-delà des 5 derniers mois.")
    col1.markdown("**:red[Cluster 0]** se situent quelque part entre les deux")

if __name__ == "__main__":
    main()
