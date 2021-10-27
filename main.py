import bokeh
from bokeh.plotting import figure, show, ColumnDataSource
from bokeh.layouts import layout, row, gridplot
from bokeh.models import Div, RangeSlider, Spinner, Button, CustomJS
from bokeh.io import curdoc
from nationality import Nation

valid_name = Nation.nationality_func('Alex')


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
          </head>
          """,
    width=200,
    height=30,
)

title = Div(
    text="""<h1 style='color: #049FD9; font-size: 34px; text-shadow: 1px 1px #58585B; border: 2px solid lightgray; padding: 7px; box-shadow: 1px 1px lightgray, -1px 1px lightgray;'>
    Predictionary</h1>""",
width=400, height=100)

title2 = Div(
    text="""<p style='color: #58585B; margin-top: -15px;'>Integrating APIs and IoT into a Custom Dashboard</p>""",
width=400, height=50)

name = Div(
    text=f"<p style='color: #58585B; margin-top: -15px;'>{valid_name}</p>",
width=400, height=50)

fig = figure(title='Line plot!', sizing_mode='scale_width')
fig.line(x=[1, 2, 3], y=[1, 4, 9])



grid = layout([
    [title],
    [title2],
    [name],
    [p, fig],
])

show(grid)