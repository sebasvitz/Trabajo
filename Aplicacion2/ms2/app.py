import dash
from dash import html
from dash import dcc
import pandas as pd 
import plotly.express as px

datos = pd.read_csv("datostiendas.csv")

fig = px.scatter_mapbox(datos , lat = "lat" , lon = "lon" , hover_name = "tienda" , hover_data = ["direccion"]
                         , color_discrete_sequence = ["fuchsia"] , zoom = 3 , height = 300)
fig.update_layout(mapbox_style = "open-street-map")
fig.update_layout(margin = {"r":0 , "t":0 , "l":0 , "b":0 })

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(children = 'Mapa de las tiendas') ,
    dcc.Graph(figure = fig)
])

if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port = 5556)

