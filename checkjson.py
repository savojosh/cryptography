import json

with open("test.json", "r") as target:
    jsondict = json.load(target)
    print(jsondict.get("S"))
    print(jsondict.get("f") + jsondict.get("R") + jsondict.get("u"))
    
    allKeysAreUnique = True

    for key in jsondict.keys():
        for f_key, f_value in jsondict.items():
            for m_key, m_value in jsondict.items():
                for b_key, b_value in jsondict.items():
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
                            print("f_key")
                            print(key + str([f_key, m_key, b_key]))
                        
                    elif(key == m_key):
                        m_location = len(f_value)
                        firstIndex = string.find(m_value)
                        secondIndex = string[firstIndex + 1:].find(m_value)

                        if(m_location != firstIndex or secondIndex != -1):
                            allKeysAreUnique = False
                            print("m_key")
                            print(key + str([f_key, m_key, b_key]))
                        
                    elif(key == b_key):
                        m_location = len(f_value + m_value)
                        firstIndex = string.find(b_value)
                        secondIndex = string[firstIndex + 1:].find(b_value)

                        if(m_location != firstIndex or secondIndex != -1):
                            allKeysAreUnique = False
                            print("b_key")
                            print(key + str([f_key, m_key, b_key]))

                    else:
                        if(string.find(jsondict.get(key)) != -1):
                            allKeysAreUnique = False
                            print("else")
                            print(key + str([f_key, m_key, b_key]))
                            print(string)
                                    
                    if(not allKeysAreUnique): break
                if(not allKeysAreUnique): break
            if(not allKeysAreUnique): 
                #print("Failed")
                break
        print(key)