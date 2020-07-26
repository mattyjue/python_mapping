import folium 
import pandas 

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elevation = list(data["ELEV"])

pib_data=pandas.read_excel("places_ive_been.xlsx")
lat1=list(pib_data["Lat"])
lon1=list(pib_data["Lon"])
population=list(pib_data["Pop"])

def elevation_color(el):
    if el < 1000:

        return 'green'
    elif 1000 <= el < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[31.2304, 100.4737], zoom_start=3, min_zoom= 1, tiles = "Stamen Terrain") #create the map and the starting locatin/zoom/ terrain and shit

fgp = folium.FeatureGroup(name="Populations") #create layer to add child class (markers)
fgp.add_child(folium.GeoJson(data= open('world.json', 'r', encoding = 'utf-8-sig').read(), 
style_function= lambda x : { 'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else  'yellow' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

fgv = folium.FeatureGroup(name="US Volcanoes") 
for lt, ln, el in zip(lat, lon, elevation): 
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, 
    popup=str(el)+"m", fill_color=elevation_color(el), color ='grey', fill_opacity=0.7))

fg_pib=folium.FeatureGroup(name="Places I've Been")
for lt, ln, p in zip(lat1, lon1, population): #for loop to add markers
    fg_pib.add_child(folium.CircleMarker(location=[lt, ln], radius=6, 
    popup=str(p), fill_color='purple', color ='purple', fill_opacity=0.7))
    
map.add_child(fgv) #add the markers (child classes)
map.add_child(fgp) 
map.add_child(fg_pib)
map.add_child(folium.LayerControl())

map.save("Map1.html") #save

