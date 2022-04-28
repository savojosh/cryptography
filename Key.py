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
    codeLength = random.randint(4,20)
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

def check_uniqueness(key):
    allKeysAreUnique = True

    for f_key, f_value in code.items():
        for m_key, m_value in code.items():
            for b_key, b_value in code.items():
                string = f_value + m_value + b_value
                #print([f_key, m_key, b_key])

                if  (key == f_key and key == m_key and key == b_key): pass
                elif(                 key == m_key and key == b_key): pass
                elif(key == f_key                  and key == b_key): pass
                elif(key == f_key and key == m_key                 ): pass

                elif(f_key == m_key or f_key == b_key): pass
                elif(m_key == b_key): pass

                elif(key == f_key):
                    firstIndex = string.find(f_value)
                    secondIndex = string[firstIndex + 1:].find(f_value)

                    if(firstIndex != 0 or secondIndex != -1):
                        allKeysAreUnique = False
                    
                elif(key == m_key):
                    m_location = len(f_value)
                    firstIndex = string.find(m_value)
                    secondIndex = string[firstIndex + 1:].find(m_value)

                    if(m_location != firstIndex or secondIndex != -1):
                        allKeysAreUnique = False
                    
                elif(key == b_key):
                    m_location = len(f_value + m_value)
                    firstIndex = string.find(b_value)
                    secondIndex = string[firstIndex + 1:].find(b_value)

                    if(m_location != firstIndex or secondIndex != -1):
                        allKeysAreUnique = False

                else:
                    if(string.find(code.get(key)) != -1):
                        allKeysAreUnique = False
                                
                if(not allKeysAreUnique): break
            if(not allKeysAreUnique): break
        if(not allKeysAreUnique): 
            #print("Failed")
            break

    return allKeysAreUnique

def create_code(name):

    global code
    allKeysAreUnique = False
    iterations = 0
    
    while(not allKeysAreUnique):
        allKeysAreUnique = True

        iterations += 1
        print("Creating Key " + str(iterations) + "...")

        for character in raw:
            code[character] = create_key()

        for key in code.keys():
            if(allKeysAreUnique):
                allKeysAreUnique = check_uniqueness(key)

        code = sort_code()

        with open(name + ".json", "w") as target:
            json.dump(code, target)

create_code("test")