import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# Fonction pour télécharger des données de disponibilité alimentaire humaine et calorique
def upload_data():
    # Demander à l'utilisateur de télécharger un fichier CSV pour les données de disponibilité alimentaire humaine
    st.markdown("### Télécharger les données de disponibilité alimentaire humaine")
    file = st.file_uploader("Sélectionner un fichier excel", type="xlsx",key='file1')
    if file is not None:
        df_dispo_humaine = pd.read_excel(file)
        st.dataframe(df_dispo_humaine.head())
    else:
        st.warning("Veuillez télécharger un fichier excel pour continuer.")

    # Demander à l'utilisateur de télécharger un fichier CSV pour les données de disponibilité calorique
    st.markdown("### Télécharger les données de disponibilité calorique")
    file = st.file_uploader("Sélectionner un fichier excel", type="xlsx",key='file2')
    if file is not None:
        df_dispo_calorique = pd.read_excel(file)
        st.dataframe(df_dispo_calorique.head())
    else:
        st.warning("Veuillez télécharger un fichier excel pour continuer.")

# Définir les options pour le dropdown
options = ["Bilan alimentaire de la Mauritanie", "Votre propre bilan alimentaire"]

# Afficher le dropdown
choice = st.selectbox("Sélectionner un titre", options)

# Si l'utilisateur choisit "Votre propre bilan alimentaire", afficher un formulaire pour télécharger les données
if choice == "Votre propre bilan alimentaire":
    upload_data()
# Sinon, afficher le bilan alimentaire de la Mauritanie
else:
    # Insérer ici le code pour afficher le bilan alimentaire de la Mauritanie
    st.write("Bilan alimentaire de la Mauritanie")




    # Setting the title on the page with some styling
    st.markdown("<h1 style='text-align: center'>Le Bilan Alimentaire de la Mauritanie en 2016 et 2017</h1><hr style='height:2px;border-width:0;color:gray;background-color:gray'>", unsafe_allow_html=True)

    # Putting in personal details with some styling
    st.markdown("<body style='text-align: center'> <b>Created by Black Group - PIE</b><br>-20020@esp.mr | 21024@esp.mr | 21035@esp.mr | 21077@esp.mr <br><a href=https://github.com/mokhtar-khalil>- Project repository on GitHub</a><hr style='height:2px;border-width:0;color:gray;background-color:gray'></body>", unsafe_allow_html=True)

    # Inserting image
    image = Image.open('ble.jpg')
    st.image(image, use_column_width=True)

    # Intro

    st.header('Introduction')
    st.markdown("Le projet PIE (Projet Industriel en Entreprise) de bilan alimentaire est un projet réalisé dans le cadre d'un élément de module par des étudiants en SID-ESP (Statistiques et Ingénierie de Données) en collaboration avec l'ANSADE (Agence Nationale de la Statistiques et de l’Analyse Démographique et Économique) et supervisé par M. Wone.")
    st.markdown("Ce projet a pour but de sensibiliser les populations sur l'importance d'une alimentation saine et équilibrée en réalisant un bilan alimentaire individuel et en proposant des recommandations personnalisées. ")
    st.markdown("Il s'inscrit dans une démarche d'éducation nutritionnelle pour lutter contre les problèmes de malnutrition et de santé publique liés à l'alimentation.")

    st.markdown("Les données utilisées dans la réalisation de ce projet sont : ")
    st.markdown(" -  La production alimentaire de la Mauritanie ")
    st.markdown(" -  Le commerce extérieur")
    st.markdown(" -  Les apports nutritionnels calorifiques")
    st.markdown("Ce projet consiste à déterminer quelques indicateurs connus internationalement dans le calcul du bilan alimentaire d'un pays qui sont : la disponibilité alimentaire humaine, la disponibilité calorifique, la disponibilité lipidique, le taux d’autosuffisance alimentaire et le taux de dépendance d’importation.")




    # Importer les données
    df_dispo = pd.read_excel("C:/Users/USER/Desktop/BILAN ALIMENTAIRE/Docs et Notebooks/disponibilite_annuelle.xlsx")
    df_cal = pd.read_excel("C:/Users/USER/Desktop/BILAN ALIMENTAIRE/Docs et Notebooks/cal1.xlsx")

    # Nettoyer les données
    df_dispo = df_dispo.drop(columns=['Unnamed: 0'])
    df_cal = df_cal.drop(columns=['Unnamed: 0'])
    df_dispo['groupe_produit'] = df_cal['groupe_produit']



    # Creating the container for the first plot
    cols = ['Comparaison entre la disponibilité alimentaire de 2016 et 2017','Comparaison entre les produits vegetaux dans la disponibilité alimentaire de 2016 et 2017','Pourcentage de contribution des produits végétaux en 2016','Pourcentage de contribution des produits végétaux en 2017']
    with st.expander(' La disponibilité alimentaire humaines (kg/pers/an)'):
        
    # Creating a selectbox dropdown with the categorical features to choose from
        cat_option = st.selectbox('Select a feature to examine', cols, key='cat_cols1')

    # The function to run the first plot
        def percentage_plot(col):

            # Creates a temporary dataframe to get the percentages
            if col ==  'Comparaison entre la disponibilité alimentaire de 2016 et 2017' :
                fig = px.line(df_dispo, x="Produit", y=['Disponibilité en 2016 (kg)','Disponibilité en 2017 (kg)'],title='Disponibilités alimentaires humaines (kg/pers/an)',
                    width=800, height=600)
            # Explaination of the features displays along with the graph
                st.markdown('**Comparaison entre la disponibilité alimentaire de 2016 et 2017:**')
                return fig
            if col ==  'Comparaison entre les produits vegetaux dans la disponibilité alimentaire de 2016 et 2017':
                dt = df_dispo[df_dispo['groupe_produit']=='Produits végétaux'].head(10)
                fig = px.line(dt, x="Produit", y=['Disponibilité en 2016 (kg)','Disponibilité en 2017 (kg)'],title='Disponibilités alimentaires humaines (kg/pers/an)',
                    width=800, height=400)
                st.markdown('**Comparaison entre les produits vegetaux dans la disponibilité alimentaire:**')
                return fig
            if col=='Pourcentage de contribution des produits végétaux en 2016':
                dt = df_dispo[df_dispo['groupe_produit']=='Produits végétaux'].head(10)
                dt['prod_pourcentage_16'] = dt['Disponibilité en 2016 (kg)'] / dt['Disponibilité en 2016 (kg)'].sum() * 100
                
                fig = px.pie(dt, values='prod_pourcentage_16', names='Produit', title='Pourcentage de contribution des produits végétaux à la disponibilité totale en 2016')
                st.markdown('**Pourcentage de contribution des produits végétaux en 2016:**')
                return fig
            if col=='Pourcentage de contribution des produits végétaux en 2017':
                dt = df_dispo[df_dispo['groupe_produit']=='Produits végétaux'].head(10)
                dt['prod_pourcentage_17'] = dt['Disponibilité en 2017 (kg)'] / dt['Disponibilité en 2017 (kg)'].sum() * 100

                fig = px.pie(dt, values='prod_pourcentage_17', names='Produit', title='Pourcentage de contribution des produits végétaux à la disponibilité totale en 2017')
                st.markdown('**Pourcentage de contribution des produits végétaux en 2017:**')
                return fig


    # Running the function
        st.plotly_chart(percentage_plot(cat_option))

    col_cal = ['Comparaison entre la disponibilité calorifique de 2016 et 2017',
                'Comparaison entre les produits vegetaux dans la disponibilité calorifique de 2016 et 2017',
                'Pourcentage de contribution des produits végétaux en 2016',
                'Pourcentage de contribution des produits végétaux en 2017']
    with st.expander(' La disponibilité calorifique (kcal/pers/an)'):
        
    # Creating a selectbox dropdown with the categorical features to choose from
        cat_option = st.selectbox('Select a feature to examine', col_cal, key='cat_cols2')


    # The function to run the first plot
        def percentage_plot(col):

            # Creates a temporary dataframe to get the percentages
            if col ==  'Comparaison entre la disponibilité calorifique de 2016 et 2017' :
                fig = px.line(df_cal, x="Produits", y=['Disponibilité par kcal (2016)','Disponibilité par kcal (2017)'],title='Disponibilités calorifique (kcal/pers/an)')
            # Explaination of the features displays along with the graph
                st.markdown('**Comparaison entre la disponibilité calorifique de 2016 et 2017:**')
                return fig
            if col ==  'Comparaison entre les produits vegetaux dans la disponibilité calorifique de 2016 et 2017':
                dt = df_cal[df_dispo['groupe_produit']=='Produits végétaux'].head(10)
                fig = px.line(dt, x="Produits", y=['Disponibilité par kcal (2016)','Disponibilité par kcal (2017)'],title='Disponibilités calorifique (kcal/pers/an)')
                st.markdown('**Comparaison entre les produits vegetaux dans la disponibilité calorifique:**')
                return fig
            if col=='Pourcentage de contribution des produits végétaux en 2016':
                dt = df_cal[df_dispo['groupe_produit']=='Produits végétaux'].sort_values(ascending=False,by=['Disponibilité par kcal (2016)','Disponibilité par kcal (2017)']).head(10)
                dt['prod_pourcentage_16'] = dt['Disponibilité par kcal (2016)'] / dt['Disponibilité par kcal (2016)'].sum() * 100
                
                fig = px.pie(dt, values='prod_pourcentage_16', names='Produits', title='Pourcentage de contribution des produits végétaux à la disponibilité en 2016')
                st.markdown('**Pourcentage de contribution des produits végétaux en 2016:**')
                return fig
            if col=='Pourcentage de contribution des produits végétaux en 2017':
                dt = df_cal[df_dispo['groupe_produit']=='Produits végétaux'].head(10)
                dt['prod_pourcentage_17'] = dt['Disponibilité par kcal (2017)'] / dt['Disponibilité par kcal (2017)'].sum() * 100

                fig = px.pie(dt, values='prod_pourcentage_17', names='Produits', title='Pourcentage de contribution des produits végétaux à la disponibilité totale en 2017')
                st.markdown('**Pourcentage de contribution des produits végétaux en 2017:**')
                return fig


    # Running the function
        st.plotly_chart(percentage_plot(cat_option))

