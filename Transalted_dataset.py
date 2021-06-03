import pandas as pd

import numpy as np

Translated_df = pd.read_csv('playas-translated-cols.csv')

Translated_df['Sea_Promenade'] = Translated_df['Sea_Promenade'].str.replace('no', 'No')

Translated_df.loc[Translated_df['Sea_Promenade']!= 'No','Sea_Promenade'] = 'Yes'

Translated_df['Nudism'] = Translated_df['Nudism'].str.replace('no', 'No')

Translated_df['Nudism'] = Translated_df['Nudism'].str.replace('Tolerado', 'Yes')

Translated_df['Nudism'] = Translated_df['Nudism'].str.replace(' ', '0')

Translated_df.loc[(Translated_df['Nudism']!= 'No') & (Translated_df['Nudism']!= 'Parcial') & (Translated_df['Nudism']!= 'Yes') & (Translated_df['Nudism']!= '0'),'Nudism'] = 'Yes'

Translated_df.loc[Translated_df['Nudism']== '0','Nudism'] = np.nan

Translated_df.loc[Translated_df['Blue_Flag']!= 'No','Blue_Flag'] = 'Yes'

Translated_df.loc[(Translated_df['Reachable_by_bus']!= 'No') & (Translated_df['Reachable_by_bus']!= ' '),'Reachable_by_bus'] = 'Yes'

Translated_df.loc[Translated_df['Reachable_by_bus']== ' ','Reachable_by_bus'] = np.nan

Translated_df.loc[(Translated_df['Parking']!= 'No') & (Translated_df['Parking']!= ' '),'Parking'] = 'Yes'

Translated_df.loc[Translated_df['Parking']== ' ','Parking'] = np.nan

Translated_df['Parking_Watched'] = Translated_df['Parking_Watched'].str.replace('No vigilado', 'No')

Translated_df['Parking_Watched'] = Translated_df['Parking_Watched'].str.replace('Vigilado', 'Yes')

Translated_df.loc[Translated_df['Parking_Watched']== ' ','Parking_Watched'] = np.nan

Translated_df.loc[Translated_df['Toilets']!= 'No','Toilets'] = 'Yes'

Translated_df.loc[(Translated_df['Footbaths']!= 'No') & (Translated_df['Footbaths']!= ' ') & (Translated_df['Footbaths']!= '-') ,'Footbaths'] = 'Yes'

Translated_df.loc[(Translated_df['Footbaths']== ' '),'Footbaths'] = np.nan

Translated_df.loc[Translated_df['Footbaths']== '-','Footbaths'] = np.nan

Translated_df.loc[Translated_df['Showers']!= 'No','Showers'] = 'Yes'

Translated_df.loc[Translated_df['Public_Telephones']!= 'No','Public_Telephones'] = 'Yes'

Translated_df.loc[Translated_df['Trashcans']!= 'No','Trashcans'] = 'Yes'

Translated_df.loc[Translated_df['Child_Zone']!= 'No','Child_Zone'] = 'Yes'

Translated_df.loc[Translated_df['Sport_Zone']!= 'No','Sport_Zone'] = 'Yes'

Translated_df.loc[Translated_df['Yacht_Club']!= 'No','Yacht_Club'] = 'Yes'

Translated_df.loc[Translated_df['Surfing_Zone']!= 'No','Surfing_Zone'] = 'Yes'

Translated_df.to_csv('playas_translated_columns_new.csv')

