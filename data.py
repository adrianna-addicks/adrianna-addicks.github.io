import pandas as pd

df=pd.read_csv('Resources/citydatainfo.csv')

df.to_html('data.html',index=False)