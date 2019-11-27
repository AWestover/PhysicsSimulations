
# this is a simple game
# get a circle of people
# they take turns saying letters
# if anyone at anytime thinks that a person has said an incorrect letter (i.e. there are no words with the current string as a prefix) then they can challenge the word and players will work this out
# bluffing is not the best strategy though tbh
# anyways people go on saying letters until someone says a word (not a proper noun) that is longer than 3 characters
# the person who says a word first loses
# the game can be played pig style, i.e. you get eliminated after saying 3 words.

import json
with open("words.json", 'r') as f:
    words = json.load(f)

with open("dictionary.json", 'r') as f:
    defns = json.load(f)

while True:
    prefix = input("What is the current game string (the prefix I have to work with) \t\t")
    wantDefns = input("Would you like definitions? (y/n)\t\t")
    # hey what about a prefix tree data structure, weren't those pretty cool!
    # eh, laziness
    # ahh the cringeiness though
    potentialWords = {}
    for w in words:
        if w[:len(prefix)] == prefix:
            try:
                potentialWords[len(w)].append(w)
            except:
                potentialWords[len(w)] = [w]

    flaggedWords = {}
    for k in potentialWords.keys():
        flaggedWords[k] = []
    for li in potentialWords.keys():
        for lo in potentialWords.keys():
            if li < lo:
                for wi in potentialWords[li]:
                    for wo in potentialWords[lo]:
                        if wo[:li] == wi:
                            flaggedWords[lo].append(wo)
    for k in flaggedWords.keys():
        for w in flaggedWords[k]:
            potentialWords[k].remove(w)

    for k in flaggedWords.keys():
        if len(potentialWords[k]) == 0:
            del potentialWords[k]

    orderedKeys = list(potentialWords.keys())    
    orderedKeys.sort() 
    for k in orderedKeys:
        print(f"Words of length \t{k}")
        for w in potentialWords[k]:
            print(f"\t{w}")
            if wantDefns == 'y':
                print(f"\t\t{defns[w][:100]}")
        print("_"*20)


