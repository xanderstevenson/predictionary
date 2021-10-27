import panel as pn
from panel.interact import interact
pn.extension()

import hvplot.pandas

import holoviews as hv
from holoviews import opts
hv.extension('bokeh')

import geoviews as gv
gv.extension('bokeh')

from vega_datasets import data as vds
from pydataset import data as pyds

from IPython.display import IFrame
documentation = IFrame(src='https://panel.holoviz.org', width=1000, height=400)
display(documentation)

