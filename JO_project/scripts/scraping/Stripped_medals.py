import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO

url = 'https://en.wikipedia.org/wiki/List_of_stripped_Olympic_medals'
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    print("Récupération du tableau principal...")
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 1er tableau 
    main_table = soup.find('table', {'class': 'wikitable'})

    if main_table:
        
        df = pd.read_html(StringIO(str(main_table)))[0]

        # Colonnes
        target_columns = ['Olympics', 'Athlete', 'Country', 'Medal', 'Event', 'Ref']
        
        current_columns = list(df.columns)
        new_columns = {}
        for i in range(min(len(current_columns), len(target_columns))):
            new_columns[current_columns[i]] = target_columns[i]
        
        df.rename(columns=new_columns, inplace=True)

        def clean(text):
            import re
            if isinstance(text, str):
                return re.sub(r'\[.*?\]', '', text).strip()
            return text

        df = df.applymap(clean)

        # Exportation en CSV
        output_file = '../../data/data_raw/Olympic_Stripped_Medals_Athletes.csv'
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        
        print(f"Le fichier '{output_file}' a été généré.")
        print("\nAperçu des premières lignes :")
        print(df[['Olympics', 'Athlete', 'Country', 'Event']].head())
    else:
        print("Erreur : Impossible de trouver le tableau principal.")

except Exception as e:
    print(f"Une erreur est survenue : {e}")
