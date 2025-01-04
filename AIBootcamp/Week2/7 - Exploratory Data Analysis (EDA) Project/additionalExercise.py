# # 1. Use another dataset and apply the same EDA steps

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Membaca file CSV dari URL
# url = "https://gist.githubusercontent.com/netj/8836201/raw/iris.csv"
# df = pd.read_csv(url)

# # Menampilkan informasi dataset
# print("Informasi Dataset:")
# print(df.info())

# # Menampilkan statistik deskriptif
# print("\nStatistik Deskriptif:")
# print(df.describe())

# # Mengecek data yang hilang
# print("\nJumlah Nilai yang Hilang:")
# print(df.isnull().sum())

# # Membuat histogram untuk distribusi kolom
# df.hist(bins=15, figsize=(10, 8), color='skyblue', edgecolor='black')
# plt.suptitle('Histograms of Iris Dataset')
# plt.show()

# # Mengeksplorasi hubungan antar fitur
# sns.pairplot(df, hue='variety', diag_kind='kde')  # Kolom 'variety' sebagai label
# plt.suptitle('Pairplot of Iris Dataset', y=1.02)
# plt.show()

# #=================================================

# # 2. Explore advanced visualizations like boxplots or pairplots in Seaborn

# # Boxplot untuk mengeksplorasi distribusi
# plt.figure(figsize=(8, 6))
# sns.boxplot(x='variety', y='sepal.length', data=df)
# plt.title('Boxplot of Sepal Length by Variety')
# plt.show()

# # Pairplot untuk visualisasi hubungan antar fitur
# sns.pairplot(df, hue='variety', kind='scatter', diag_kind='kde')
# plt.suptitle('Pairplot of Iris Dataset with KDE', y=1.02)
# plt.show()

#=====================================================

# 3. Create a dashboard for your findings using Plotly or Dash

import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Membaca dataset dari URL
url = "https://gist.githubusercontent.com/netj/8836201/raw/iris.csv"
df = pd.read_csv(url)

# Membuat dashboard dengan Dash
app = dash.Dash(__name__)

# Layout dashboard
app.layout = html.Div([
    html.H1("Iris Dataset Dashboard"),
    
    dcc.Dropdown(
        id='feature-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns if col != 'variety'],
        value='sepal.length',
        placeholder='Select a feature to visualize'
    ),
    
    dcc.Graph(id='boxplot-graph'),
    
    dcc.Graph(
        id='scatter-graph',
        figure=px.scatter_matrix(
            df,
            dimensions=['sepal.length', 'sepal.width', 'petal.length', 'petal.width'],
            color='variety',
            title="Scatter Matrix of Iris Dataset"
        )
    )
])

# Callback untuk memperbarui boxplot berdasarkan fitur yang dipilih
@app.callback(
    Output('boxplot-graph', 'figure'),
    [Input('feature-dropdown', 'value')]
)
def update_boxplot(feature):
    fig = px.box(df, x='variety', y=feature, color='variety', title=f"Boxplot of {feature} by Variety")
    return fig

# Menjalankan aplikasi Dash
if __name__ == '__main__':
    app.run_server(debug=True)
