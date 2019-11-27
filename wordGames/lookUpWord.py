
import json

with open("dictionary.json", 'r') as f:
    data = json.load(f)

while True:
    word = input("Word: \t").strip()
    try:
        print(data[word])
    except:
        print("that string does not occur in the dictionary")
    print("-"*100)

