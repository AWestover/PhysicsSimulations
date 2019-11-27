
import json

# I got this json from https://github.com/matthewreagan/WebstersEnglishDictionary
with open("dictionary.json", 'r') as f:
    data = json.load(f)

data = list(filter(lambda x: (" " not in x) and ("-" not in x), data.keys()))

with open("words.json", 'w') as f:
    json.dump(data, f)


