import dash
import dash_core_components as dcc
import dash_html_components as html
import json
from textwrap import dedent as d
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np

#Read dataset
df = pd.read_csv("Detector_1.csv")
df1 = pd.read_csv("Detector_2.csv")
df2 = pd.read_csv("Detector_3.csv")
#List of dataset columns
available_indicators = list(df)
available_indicators = list(df1)
available_indicators = list(df2)

#Initialize Dash
app = dash.Dash()

app = dash.Dash(__name__)
app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

app.layout = html.Div([
    
    html.Div([
        html.H1('Detectors Data Analysis',style={"textAlign": "center"}),
        html.P('By: Keerthi Prakash')],style = {'padding' : '50px' ,'backgroundColor' : '#3aaab2', "textAlign": "center"}),
         dcc.Markdown('''
Welcome to my Plotly (Dash) Data Science interactive dashboard. In order to create this dashboard have been used different datasets.
We plotted the hourly distribution of each detector by histogram plot. 
Plotting the hourly distribution for each detector shows us that, in general, the detectors peak in the
afternoon and are much less likely to be triggered during the night and early morning 
which may implicate that the triggering objects are biological in nature (or tied to the day-night cycle)''')  ,
     
    
    html.H1("Detectors Hourly Distribution Histogram Plot", style={'textAlign': 'center', 'padding-top': 5}),
    dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': df['Hour'],
                    'text': df['Hour'],
                    'customdata': df['DateTime'],
                    'name': 'Detector 1 - Hourly Distribution',
                    'type': 'histogram'
                },
                {
                    'x': df1['Hour'],
                    'text': df1['Hour'],
                    'customdata': df1['DateTime'],
                    'name': 'Detector 2 - Hourly Distribution',
                    'type': 'histogram'
                },
                {
                    'x': df2['Hour'],
                    'text': df2['Hour'],
                    'customdata': df2['DateTime'],
                    'name': 'Detector 3 - Hourly Distribution',
                    'type': 'histogram'
                }
                
            ],
            
            'layout': {}
        }
    ),

    html.Div(className='row', children=[
        html.Div([
            dcc.Markdown(d("""
                **Hover Data**
                Mouse over values in the graph.
            """)),
            html.Pre(id='hover-data', style=styles['pre'])
        ], className='three columns'),

        html.Div([
            dcc.Markdown(d("""
                **Click Data**
                Click on points in the graph.
            """)),
            html.Pre(id='click-data', style=styles['pre']),
        ], className='three columns'),

        html.Div([
            dcc.Markdown(d("""
                **Selection Data**
                Choose the lasso or rectangle tool in the graph's menu
                bar and then select points in the graph.
            """)),
            html.Pre(id='selected-data', style=styles['pre']),
        ], className='three columns'),

        html.Div([
            dcc.Markdown(d("""
                **Zoom and Relayout Data**
                Click and drag on the graph to zoom or click on the zoom
                buttons in the graph's menu bar.
                Clicking on legend items will also fire
                this event.
            """)),
            html.Pre(id='relayout-data', style=styles['pre']),
        ], className='three columns')
    ])
])

@app.callback(
     Output ('hover-data', 'children'),
    [Input('basic-interactions', 'hoverData')])
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)


@app.callback(
    Output('click-data', 'children'),
    [Input('basic-interactions', 'clickData')])
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)


@app.callback(
    Output('selected-data', 'children'),
    [Input('basic-interactions', 'selectedData')])
def display_selected_data(selectedData):
    return json.dumps(selectedData, indent=2)


@app.callback(
    Output('relayout-data', 'children'),
    [Input('basic-interactions', 'relayoutData')])
def display_selected_data(relayoutData):
    return json.dumps(relayoutData, indent=2)

if __name__ == '__main__':
    app.run_server(debug=True)
