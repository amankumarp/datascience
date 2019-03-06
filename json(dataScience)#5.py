import json
myjson='''
{
"status":"ok",
"source":"this",
"value":"uid"
}
'''
a=json.loads(myjson)
print(a["source"])