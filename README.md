Analyse des Jeux Olympiques
Projet Data Analysis – Certification Jedha
Contexte
Ce projet a été réalisé dans le cadre de la certification Jedha – Formation Fullstack Data Analysis, sous la forme d’un projet de groupe.

Les Jeux Olympiques représentent l’un des événements sportifs les plus emblématiques au monde. À travers plus d’un siècle d’histoire et 63 éditions, ils offrent un terrain d’analyse riche permettant d’étudier à la fois les performances sportives, l’évolution des disciplines et les enjeux d’intégrité du sport.

Problématique
Comprendre l’évolution des Jeux Olympiques à travers le temps.

Objectifs du projet
Réaliser une analyse multidimensionnelle des performances olympiques, en croisant plusieurs axes :

Succès sportifs : médailles, pays, sports et athlètes
Évolution des disciplines et des épreuves olympiques
Caractéristiques des athlètes (genre, participation, récurrence)
Intégrité du sport : analyse des cas de dopage et des médailles retirées
L’objectif final est de produire des visualisations claires et exploitables, intégrées dans un dashboard Power BI, afin de faciliter l’analyse et la prise de décision.

Sources de données
Données issues de Kaggle
Les données principales du projet proviennent du dataset Kaggle suivant :

🔗 120 Years of Olympic History: Athletes and Results
https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results

Fichiers utilisés :

Olympic_Athlete_Bio.csv
Olympic_Athlete_Event_Results.csv
Olympic_Games_Medal_Tally.csv
Olympic_Results.csv
Olympics_Country.csv
Olympics_Games.csv
🌐 Données scrappées depuis Wikipédia – Médailles retirées
🔗 https://en.wikipedia.org/wiki/List_of_stripped_Olympic_medals

Fichiers concernés :

Olympic_Stripped_Medals_Athletes.csv
Olympic_Stripped_Medals_Country.xlsx
Olympic_Stripped_Medals_Gender.csv
Olympic_Stripped_Medals_Sport.csv
🌍 Données scrappées depuis Wikipédia – Codes CIO
🔗 https://fr.wikipedia.org/wiki/Liste_des_codes_pays_du_CIO

Fichier utilisé :

codes_cio_new_test.json
🌍 Autres sources
Mapping pays → continent
🔗 https://github.com/subyfly/topojson/blob/master/world-continents.json
🛠️ Technologies utilisées
Langage
Python
Librairies
pandas
numpy
seaborn
matplotlib.pyplot
plotly.express
plotly.graph_objects
requests
re
BeautifulSoup
StringIO
Data Visualization / BI
Power BI
Autres outils
Mapshaper - nettoyage et simplification de fichiers géographiques https://mapshaper.org/

🏗️ Architecture du projet

JO_project/ ├── scripts/ │ ├── 00_nettoyage_data_raw.ipynb │ ├── 01_visualisation_eda.ipynb │ └── webscraping/ │ │ ├── Flags.py │ │ ├── Stripped_medals.py │ │ ├── Stripped_medals_by_gender.py │ │ ├── Stripped_medals_by_sport.py │ │ └── Stripped_medals_list.py │ ├── data/ │ ├── data_raw/ │ └── data_clean/ │ ├── visualisation/ │ ├── README.md └── .gitignore

Description des notebooks
00_nettoyage_data_raw.ipynb
Nettoyage de l’ensemble des fichiers CSV et JSON issus des différentes sources
Harmonisation des formats et des nomenclatures
Typage et normalisation des colonnes
Suppression des doublons et des incohérences
Création de nouvelles tables analytiques
Production des datasets clean
01_visualisation_eda.ipynb
Analyse exploratoire des données nettoyées
Création des premières visualisations
Identification des indicateurs clés
Préparation des graphiques pour Power BI
Livrables
Dashboard Power BI
Notebooks Python
Exports CSV & JSON
Présentation PowerPoint
Équipe projet
BRETTON Stephanie
BREUILLARD Maxime
CARTIGNY Simon
PAGET Pierre-Alexandre
Évolutions possibles
Ajout des nouvelles éditions des Jeux Olympiques
Intégration des Jeux Olympiques Paralympiques
Nouvelles analyses géopolitiques et économiques
Licence
Projet à but pédagogique utilisant exclusivement des données publiques.
