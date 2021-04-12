import pandas as pd
import plotly.express as px
df=pd.read_csv(r"C:\Users\a2z\Downloads\Data-visualization-master\Data-visualization-master\csv files\data.csv")
fig=px.scatter(df,x="Population",y="Per capita",size="Population",color="Country",title="Data of Various Countries")
fig.show()