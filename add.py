import json
import os
from pathlib import Path

f = open("recipes.json", "r")

jsondata = json.loads(f.read())
print(jsondata)
f.close()
files = os.listdir("./recipes")
print(files)
for f in files:
  key = Path(f).stem
  title =  key.replace("_", " ").title()
  filename = f
  jsondata["items"][key] = {"title": title, "filename": filename}
print(jsondata)  

with open("recipes.json", "w") as outfile:
  json.dump(jsondata, outfile, indent=4, sort_keys=True)