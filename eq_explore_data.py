import json

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline


# Explore the structure of the data
filename = '/home/renato/Documents/data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

text_file = all_eq_data['metadata']
all_eq_data = all_eq_data['features']

mags, lons, lats, hover_text = [],[],[],[]
for eq_dict in all_eq_data:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_text.append(eq_dict['properties']['title'])


show_textfile = text_file['title']
# Map the earthquakes
data = [{
    'type':'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker':{
        'size': [3*mag for mag in mags],
        'color': mags,
        'colorscale':'YlGnBu',
        'reversescale':True,
        'colorbar':{
            'title':'Magnitude',
        },
    }

}]

my_layout = Layout(title=show_textfile)

fig = {'data':data, 'layout':my_layout}
offline.plot(fig,filename='global_earthqueakes.html')


#readable_file = '/home/renato/Documents/data/readable_eq_data.json'
#with open(readable_file) as f:
#    json.dump(all_eq_data, f, indent=4)