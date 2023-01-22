import pandas as pd
import folium
from folium.plugins import MarkerCluster    # Import folium MousePosition plugin
from folium.plugins import MousePosition    # Import folium DivIcon plugin
from folium.features import DivIcon

df = pd.read_csv('zillow.csv')
drawable_df = df[df.Lat > 0.0]

mapit = folium.Map( location=[49.261505,  -123.05453], zoom_start=12 )
for index, drawable_df in drawable_df.iterrows():
    if drawable_df["TypeofProperty"]=='Condo':   c = 'blue'
    elif drawable_df["TypeofProperty"]=='Townhouse':    c = 'green'
    elif     drawable_df["TypeofProperty"]=='Multi-family home':  c = 'gray'
    else:
        c = 'red'
    folium.Marker(
                location = [drawable_df['Lat'], drawable_df['Long']],
                radius=15 ,
                icon=folium.Icon(color= c ) ,
                popup = f'Type:{drawable_df["TypeofProperty"]}\n Price($):{drawable_df["Price"]}'
                ).add_to(mapit)
mapit.save('map.html')
mapit.show_in_browser()
