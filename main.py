import bokeh
from bokeh.palettes import Category20c
from bokeh.transform import cumsum
from bokeh.plotting import figure, show, ColumnDataSource
from bokeh.layouts import layout, row, gridplot
from bokeh.models import Div, RangeSlider, Spinner, Button, CustomJS
from bokeh.io import curdoc
from nationality import Nation
from dashboard import Dash
from math import pi
import pandas


valid_name = Dash().valid_name
valid_name = valid_name.capitalize()
country_1 = Dash().country_1
country_2 = Dash().country_2
country_3 = Dash().country_3
age = Dash().age
gender = Dash().gender.capitalize()
gender_prob = Dash().gender_prob


# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# create plot with circle glyphs
p = figure(x_range=(1, 9), width=500, height=250)
points = p.circle(x=x, y=y, size=30, fill_color="#21a7df")


# header

header = Div(
    text="""
          <head>
          <link rel="stylesheet" href="css/styles.css"/>
          <link rel="stylesheet" href="static/css/styles.css">
          <link rel="stylesheet" href="dashboard/static/css/styles.css"/>
          <style> body {background-color:silver>}</style>
          </head>
          """,
    width=200,
    height=30,
)

title = Div(
    text="""<h1 style='color: #049FD9; font-size: 34px; text-shadow: 1px 1px #58585B; border: 2px solid lightgray; padding: 9px; box-shadow: 1px 1px lightgray, -1px 1px lightgray;'>
    Predictionary</h1>""",
width=400, height=100)

title2 = Div(
    text="""<p style='font-size: 28; color: #58585B; margin-top: -15px;'>Integrating APIs and IoT into a Custom Dashboard</p>""",
width=400, height=50)

name = Div(
    text=f"<p style='fcolor: #58585B; margin-top: -15px;'>Name: {valid_name} <br>Nation: {country_1}, {country_2}, {country_3}<br>Age: {age} <br>Gender: {gender} {gender_prob}</p>",
width=400, height=50)



# GENDER GRAPH

gender_prob = gender_prob[:-1]
if gender == 'Male':

    x = {
        'Male': int(gender_prob),
        'Female': 100 - int(gender_prob)
    }

else:
    x = {
    'Female': int(gender_prob),
    'Male': 100 - int(gender_prob)
    }


data = pandas.Series(x).reset_index(name='value').rename(columns={'index': 'country'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = ['#049FD9', '#004BAF']

gender_graph = figure(height=350, width=350, title=f"Gender: {gender}, Probability: {gender_prob}%", toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

gender_graph.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='country', source=data)

gender_graph.axis.axis_label = None
gender_graph.axis.visible = False
gender_graph.grid.grid_line_color = None



# GRID LAYOUT

grid = layout([
    [title],
    [title2],
    [name],
    [gender_graph]
])
show(grid)