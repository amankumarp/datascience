import pandas as pd

prices=[[71,32,34],[54,54,23],[23,44,23],[54,54,3],[5,5,3],[4,4,2]]

simple_dataframe=pd.DataFrame(prices)
print(simple_dataframe)
header_dataframe=pd.DataFrame(prices,columns=['jan','feb','march'])
print(header_dataframe)
print(header_dataframe['feb'][0])
print("first five row are")
print(header_dataframe.head())
print("last five row")
print(header_dataframe.tail())
