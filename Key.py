import os
import json
import random
import time

raw = [
    "A","a",
    "B","b",
    "C","c",
    "D","d",
    "E","e",
    "F","f",
    "G","g",
    "H","h",
    "I","i",
    "J","j",
    "K","k",
    "L","l",
    "M","m",
    "N","n",
    "O","o",
    "P","p",
    "Q","q",
    "R","r",
    "S","s",
    "T","t",
    "U","u",
    "V","v",
    "W","w",
    "X","x",
    "Y","y",
    "Z","z",
    "1","2","3","4","5","6","7","8","9","0",
    "!","@","#","$","%","^","&","*","(",")",
    "_","-",
    "+","=",
    "~","`",
    "{","[",
    "}","]",
    "|",#"\\",
    ":",";",
    #"'",""",
    "<",",",
    ">",".",
    "?","/"
]

code = {}

def create_key():
    codeLength = random.randint(4,10)
    key = ""

    for x in range(codeLength):
        key = key + raw[random.randint(0, len(raw) - 1)]
    
    # clock = str(time.time())
    # key = key + clock[(len(clock) - 2):]

    for entry in code.keys():
        if(code.get(entry).find(key) != -1):
            key = create_key()

    return key

def sort_code():
    newCode = {}
    sortedKeys = []
    
    for item in code.items():
        key = item[0]
        value = item[1]
        index = 0
        edited = False

        if(len(sortedKeys) == 0):
            sortedKeys = [key]
        else:
            while(index < len(sortedKeys) and not edited):
                
                if(len(value) >= len(code.get(sortedKeys[index]))):
                    sortedKeys.insert(index, key)
                    edited = True
                elif(index >= len(sortedKeys) - 1):
                    sortedKeys.append(key)
                    edited = True
            
                index += 1
    
    for key in sortedKeys:
        newCode[key] = code.get(key)

    return newCode

def create_code(name):

    global code
    allKeysAreUnique = False

    iteration = 0
    
    while(not allKeysAreUnique):
        allKeys = ""
        iteration += 1

        for character in raw:
            code[character] = create_key()
            allKeys = allKeys + code.get(character)

        for key, value in code.items():
            firstIndex = allKeys.find(value)
            secondIndex = allKeys[firstIndex + 1:].find(value)

            if(secondIndex == -1):
                allKeysAreUnique = True
            else:
                allKeysAreUnique = False
    
    code = sort_code()

    with open(name + ".json", "w") as target:
        json.dump(code, target)

create_code("test")