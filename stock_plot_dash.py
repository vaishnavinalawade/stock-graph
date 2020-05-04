# -*- coding: utf-8 -*-
"""
Created on Sun May  3 05:50:08 2020

@author: Vaish
"""
import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children = [
        html.Div(children = ''' Stock Symbol to Graph '''),
        dcc.Input(id='input', value='CBS', type='text'),
        html.Div(dcc.Graph(id='output-graph'))])

@app.callback(Output(component_id='output-graph', component_property='figure'),
              [Input(component_id='input', component_property='value')])
def update_graph(input_data):
    start = datetime.datetime(2017, 1, 1)
    end = datetime.datetime.now()
    df = web.get_data_yahoo(input_data, start=start, end=end)
    df.reset_index(inplace=True)
    '''df.set_index("Date", inplace=True)
    df = df.drop("Symbol", axis=1)'''
     
    return {'data':[{'x':df.index,'y':df.Close,'type': 'line','name':input_data}],
                    'layout':{'title':input_data}}

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
        