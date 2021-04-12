import pandas as pd 
import plotly.express as px
df=pd.read_csv(r"C:\Users\a2z\Downloads\Data-visualization-master\Data-visualization-master\csv files\line_chart.csv")
fig=px.bar(df,x="Year",y="Per capita income",color="Country",title="Data Over the Years of Different Countries")
fig.show()