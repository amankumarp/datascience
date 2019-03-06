import pandas as pd

prices=[[71,32,34],[54,54,23],[23,44,23],[54,54,3],[5,5,3],[4,4,2]]

# simple_dataframe=pd.DataFrame(prices)
# print(simple_dataframe)
header_dataframe=pd.DataFrame(prices,columns=['jan','feb','march'])
pd.DataFrame(header_dataframe).to_csv('output .csv')