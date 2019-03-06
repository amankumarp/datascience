import urllib.request as urlr
import json
raw=url.urlopen("")  #give the json news api key
print(raw.read())
myjson=raw.read()
a=json.loads(myjson.decode())
for i in range(0,5):
    print("Headline number "+str(i+1)+"is")
    print(a['articles'][i]['title'])

