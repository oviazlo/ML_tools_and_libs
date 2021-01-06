import plotly as py
import pandas as pd
import plotly.express as px
from sklearn.datasets import make_blobs
py.offline.init_notebook_mode(connected=True)


def get_cluster_data():
    centers = [(-5, -5, -5), (5, 5, 5), (4, 5, 4.5)]
    cluster_std = [0.8, 1, 0.5]
    X, y = make_blobs(n_samples=100, cluster_std=cluster_std, centers=centers, n_features=3, random_state=1)
    df = pd.DataFrame(X, columns=['x', 'y', 'z'])
    df['cluster_id'] = y
    return df


# Options to draw
# 0 - draw cluster data made with make_blobs
# 1 - draw example from Kaggle House price competition
draw_option = 1

if draw_option == 0:
    data = get_cluster_data()
    fig = px.scatter_3d(data, x="x", y="y", z="z", color='cluster_id')

if draw_option == 1:
    data = pd.read_csv("data/kaggle_house_prices_train_data.csv")
    fig = px.scatter_3d(data, x="LotArea", y="GarageArea", z="SalePrice", color="GarageCars")

fig.write_html("plot_3d.html")
