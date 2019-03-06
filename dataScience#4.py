import quandl
dataset=quandl.get("CHRIS/ASX_WM2")  # it quandal data
print(dataset)
print(dataset['Previous Settlement'][0])