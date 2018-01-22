import dash; from dash.dependencies import Input, Output
import dash; from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd; import plotly.graph_objs as go
from datetime import datetime

import os

lapp = dash.Dash()
server = lapp.server
server.secret_key = os.environ.get('SECRET_KEY', 'my-secret-key')

# layout
lapp.layout = html.Div(children=[
    html.H1(children='Suicide rates in Germany, 1979'),

    html.P(children='''
	Data from Heuer (1979) on suicide rates in West Germany classified by age, sex, and method of suicide.
        A data frame with 306 observations and 6 variables.
    '''),
    html.Br(),    

    dcc.Graph(
        id='example-graph',
    ),
    dcc.Dropdown(
        options=[
            {'label': 'Frequency by method', 'value': 'freqbymethod'},
            {'label': 'Method by age', 'value': 'age'},
            {'label': 'Frequency by sex', 'value': 'freqsex'},
            {'label': 'Age by sex', 'value': 'agesex'},
            {'label': 'Method by sex', 'value': 'metsex'}
        ],
        value='freqbymethod',
        id = 'dropdown_input'
    ),
    html.Br(),
    dcc.RadioItems(
        options=[
            {'label': 'Barplot', 'value': 'hist'},
            {'label': 'Boxplot', 'value': 'boxplot'}
        ],
        value='hist',
        id='radio-input'
    ),
    html.Br(),
    dcc.Graph(id='example-graph'),
    html.Div(children='''
        Data:
    '''),
    html.Div(style={'font-style': 'italic'}, children=[
        html.P('https://raw.githubusercontent.com/lycanea/python_biol_2017/master/suicide.csv')
    ]),
    html.Div(children='''
        Dataset information:
    '''),

    html.Div(style={'font-style': 'italic'}, children=[
        html.P('https://vincentarelbundock.github.io/Rdatasets/doc/vcd/Suicide.html')
    ])
])

@lapp.callback(
    Output(component_id='example-graph', component_property='figure'),
    [Input(component_id='radio-input', component_property='value'),
    Input(component_id='dropdown_input', component_property='value')]
)
def update_figure(plot_type, data_type):
   
    if plot_type == "hist" and data_type == "age":
    	trace1 = go.Histogram(x = knife_age.age, name = 'knife')
    	trace2 = go.Histogram(x = drown_age.age, name = 'drown')
    	trace3 = go.Histogram(x = hang_age.age, name = 'hang')
    	trace4 = go.Histogram(x = jump_age.age, name = 'jump')
    	trace5 = go.Histogram(x = gas_age.age, name = 'gas')
    	trace6 = go.Histogram(x = gun_age.age, name = 'gun')
    	trace7 = go.Histogram(x = poison_age.age, name = 'poison')
    	trace8 = go.Histogram(x = other_age.age, name = 'other')

    	data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8]

    elif plot_type == "hist" and data_type == "freqbymethod":
    	trace1 = go.Histogram(x = suicide.method2,y = suicide.Freq, name = 'Frequency')
    	trace2 = go.Histogram(x = drown_age.sex,y = suicide.Freq, name = 'drown')
    	trace3 = go.Histogram(x = hang_age.sex,y = suicide.Freq, name = 'hang')
    	trace4 = go.Histogram(x = jump_age.sex,y = suicide.Freq, name = 'jump')
    	trace5 = go.Histogram(x = gas_age.sex,y = suicide.Freq, name = 'gas')
    	trace6 = go.Histogram(x = gun_age.sex,y = suicide.Freq, name = 'gun')
    	trace7 = go.Histogram(x = poison_age.sex,y = suicide.Freq, name = 'poison')
    	trace8 = go.Histogram(x = other_age.sex,y = suicide.Freq, name = 'other')

    	data = [trace1]

    elif plot_type == "hist" and data_type == "freqsex":
        trace1 = go.Histogram(x = female.sex, y= female.Freq,name = "female")
        trace2 = go.Histogram(x = male.sex, y= male.Freq,name = "male")        
        
        data = [trace1, trace2]

    elif plot_type == "hist" and data_type == "agesex":
        trace1 = go.Histogram(x = male.age,name = "male")
        trace2 = go.Histogram(x = female.age,name = "female")        
        
        data = [trace1, trace2]

    elif plot_type == "hist" and data_type == "metsex":
    	trace1 = go.Histogram(x = knife_age.sex, name = 'knife')
    	trace2 = go.Histogram(x = drown_age.sex, name = 'drown')
    	trace3 = go.Histogram(x = hang_age.sex, name = 'hang')
    	trace4 = go.Histogram(x = jump_age.sex, name = 'jump')
    	trace5 = go.Histogram(x = gas_age.sex, name = 'gas')
    	trace6 = go.Histogram(x = gun_age.sex, name = 'gun')
    	trace7 = go.Histogram(x = poison_age.sex, name = 'poison')
    	trace8 = go.Histogram(x = other_age.sex, name = 'other')

    	data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8]

    elif plot_type == "boxplot" and data_type == "age":
    	trace1 = go.Box(y = knife_age.age, opacity = 0.75, name = 'knife')
    	trace2 = go.Box(y = drown_age.age, opacity = 0.75, name = 'drown')
    	trace3 = go.Box(y = hang_age.age, opacity = 0.75, name = 'hang')
    	trace4 = go.Box(y = jump_age.age, opacity = 0.75, name = 'jump')
    	trace5 = go.Box(y = gas_age.age, opacity = 0.75, name = 'gas')
    	trace6 = go.Box(y = gun_age.age, opacity = 0.75, name = 'gun')
    	trace7 = go.Box(y = poison_age.age, opacity = 0.75, name = 'poison')
    	trace8 = go.Box(y = other_age.age, opacity = 0.75, name = 'other')

    	data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8]

    elif plot_type == "boxplot" and data_type == "Freq":
    	trace1 = go.Box(y = knife_age.Freq, opacity = 0.75, name = 'knife')
    	trace2 = go.Box(y = drown_age.Freq, opacity = 0.75, name = 'drown')
    	trace3 = go.Box(y = hang_age.Freq, opacity = 0.75, name = 'hang')
    	trace4 = go.Box(y = jump_age.Freq, opacity = 0.75, name = 'jump')
    	trace5 = go.Box(y = gas_age.Freq, opacity = 0.75, name = 'gas')
    	trace8 = go.Box(y = other_age.Freq, opacity = 0.75, name = 'other')
    	trace6 = go.Box(y = gun_age.Freq, opacity = 0.75, name = 'gun')
    	trace7 = go.Box(y = poison_age.Freq, opacity = 0.75, name = 'poison')  

    	data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8]



    elif plot_type == "boxplot" and data_type == "metsex":
    	trace1 = go.Box(y = knife_male.Freq, opacity = 0.75, name = 'knife male')
    	trace11 = go.Box(y = knife_female.Freq, opacity = 0.75, name = 'knife female')
    	trace2 = go.Box(y = drown_male.Freq, opacity = 0.75, name = 'drown male')
    	trace21 = go.Box(y = drown_female.Freq, opacity = 0.75, name = 'drown female')
    	trace3 = go.Box(y = hang_male.Freq, opacity = 0.75, name = 'hang male')
    	trace31 = go.Box(y = hang_female.Freq, opacity = 0.75, name = 'hang female')
    	trace4 = go.Box(y = jump_male.Freq, opacity = 0.75, name = 'jump male')
    	trace41 = go.Box(y = jump_female.Freq, opacity = 0.75, name = 'jump female')
    	trace5 = go.Box(y = gas_male.Freq, opacity = 0.75, name = 'gas male')
    	trace51 = go.Box(y = gas_female.Freq, opacity = 0.75, name = 'gas female')
    	trace8 = go.Box(y = other_male.Freq, opacity = 0.75, name = 'other male')
    	trace81 = go.Box(y = other_female.Freq, opacity = 0.75, name = 'other female')
    	trace7 = go.Box(y = gun_male.Freq, opacity = 0.75, name = 'gun male')
    	trace71 = go.Box(y = gun_female.Freq, opacity = 0.75, name = 'gun female')
    	trace6 = go.Box(y = poison_male.Freq, opacity = 0.75, name = 'poison male')
    	trace61 = go.Box(y = poison_female.Freq, opacity = 0.75, name = 'poison female')

    	data = [trace1, trace11, trace2, trace21, trace3, trace31, trace4,trace41, trace5, trace51, trace6, trace61, trace7, trace71, trace8, trace81]


    elif plot_type == 'boxplot' and data_type == "agesex":
        trace1 = go.Box(y = male.age,name = "male")
        trace2 = go.Box(y = female.age,name = "female")        
        
        data = [trace1, trace2]

    elif plot_type == 'boxplot' and data_type == "freqsex":
        trace1 = go.Box(x = female.sex, y= female.Freq,name = "female")
        trace2 = go.Box(x = male.sex, y= male.Freq,name = "male")           
        
        data = [trace1, trace2]

    elif plot_type == 'boxplot' and data_type == "freqbymethod":
        trace1 = go.Box(x = suicide.method2, y= suicide.Freq,name = "frequency")

        data = [trace1]
    figure={
        'data': data,
        'layout': {
            'title': '',
            'showlegend': True,
        },
    }
    return figure

suicide=pd.read_csv("https://raw.githubusercontent.com/lycanea/python_biol_2017/master/suicide.csv")
suicide=suicide.rename(index=str, columns={"Unnamed: 0": "a"})


knife_age = suicide[suicide.method2=="knife"]
drown_age = suicide[suicide.method2=="drown"]
hang_age = suicide[suicide.method2=="hang"]
jump_age = suicide[suicide.method2=="jump"]
gas_age = suicide[suicide.method2=="gas"]
other_age = suicide[suicide.method2=="other"]
gun_age = suicide[suicide.method2=="gun"]
poison_age = suicide[suicide.method2=="poison"]
method_age=[knife_age, drown_age, hang_age, jump_age, gas_age, other_age, gun_age, poison_age]
female = suicide[suicide.sex =="female"]
male = suicide[suicide.sex =="male"]
sexx = [female, male]
knife_male = knife_age[knife_age.sex=="male"]
drown_male = drown_age[drown_age.sex=="male"]
hang_male = hang_age[hang_age.sex=="male"]
jump_male = jump_age[jump_age.sex=="male"]
gas_male = gas_age[gas_age.sex=="male"]
other_male = other_age[other_age.sex=="male"]
gun_male = gun_age[gun_age.sex=="male"]
poison_male = poison_age[poison_age.sex=="male"]
knife_female = knife_age[knife_age.sex=="female"]
drown_female = drown_age[drown_age.sex=="female"]
hang_female = hang_age[hang_age.sex=="female"]
jump_female = jump_age[jump_age.sex=="female"]
gas_female = gas_age[gas_age.sex=="female"]
other_female = other_age[other_age.sex=="female"]
gun_female = gun_age[gun_age.sex=="female"]
poison_female = poison_age[poison_age.sex=="female"]

# run
if __name__ == '__main__':
    lapp.run_server(debug=True)
