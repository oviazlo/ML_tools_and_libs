import plotly as py
py.offline.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import numpy as np

y = np.random.randn(500)
data = [go.Histogram(y=y)]

py.offline.plot(data, filename='plot_2d.html')
