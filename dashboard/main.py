import bokeh
from bokeh.plotting import figure, show, ColumnDataSource
from bokeh.layouts import layout
from bokeh.models import Div, RangeSlider, Spinner, Button, CustomJS
from bokeh.io import curdoc

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

# set up textarea (div)
div = Div(
    text="""
          <p>Select the circle's size using this control element:</p>
          """,
    width=200,
    height=30,
)

# set up spinner
spinner = Spinner(
    title="Circle size",
    low=0,
    high=60,
    step=5,
    value=points.glyph.size,
    width=200,
)
spinner.js_link("value", points.glyph, "size")

title = Div(
    text="""<h1 style='color: #049FD9; font-size: 34px; text-shadow: 1px 1px #58585B'>Predictionary</h1>""",
width=400, height=100)


fig = figure(title='Line plot!', sizing_mode='scale_width')
fig.line(x=[1, 2, 3], y=[1, 4, 9])

# curdoc().title = "Hello, world!"
# curdoc().add_root(fig)

layout = layout(
    [
        [title],
        [p],
        [div, spinner],
        [fig],
    ]
)

show(layout)