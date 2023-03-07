import pandas as pd
df=pd.read_csv('C:\\NetworkingProject\packet_capture\capturedpacket.csv')
print(df.columns)
print(df.groupby('Protocol').sum())