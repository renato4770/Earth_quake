import csv
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data
filename = '/home/renato/Documents/data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    title = "World Fires"

    brights, lons, lats, hover_text = [],[],[], []
    for row in reader:
        brights.append(row[2])
        lons.append(row[1])
        lats.append(row[0])
        hover_text.append(float(row[3]))

    # Map the world fires
    data = [{
        'type':'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_text,
        'marker':{
            'size': [2*hover_text1 for hover_text1 in hover_text],
            'color': hover_text,
            'colorscale':'YlGnBu',
            'reversescale':True,
            'colorbar':{
                'title':'Fire Level',
            },
        }

    }]
    my_layout = Layout(title=title)

    fig = {'data':data, 'layout':my_layout}
    offline.plot(fig,filename='world_fires.html')