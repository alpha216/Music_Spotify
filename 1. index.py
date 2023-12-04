import json
 
w = open("src/Library.json", "r")
data = json.load(w)

data = data["Tracks"]

temp = []

for i in data.values():
    temp.append([i["Name"], i["Artist"], i["Album"], i["Genre"], i["Year"]])
    
w = open("src/shorted.json", "w")
w.write(json.dumps(temp, ensure_ascii=False))
w.close()