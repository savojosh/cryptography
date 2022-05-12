import os
import json
import Key

def translate_text(code, nums, text):
    translation = ""
    translation_num = 0

    nums_file = open(nums, "r")
    nums_dictionary = json.load(nums_file)
    nums_source = nums_dictionary.get("nums")
    nums_file.close()

    for character in text:
        if(character == " "):
            translation += character
        elif(character != ""):
            #print(character + " " + Key.translate_num_to_key(code, character, nums_source[translation_num]) + " " + str(nums_source[translation_num]))
            translation += Key.translate_char_to_key(code, character, nums_source[translation_num])
            #print(translation)
            translation_num += 1
        
        if(translation_num >= len(nums_source)):
            translation_num = 0
        
    return translation

def translate_file(code, nums, absoluteFilePath):

    file = open(absoluteFilePath, "r")
    file_name = os.path.basename(absoluteFilePath)
    file_ext = os.path.splitext(absoluteFilePath)[1]
    file_name = file_name[:len(file_name) - len(file_ext)]

    if(os.path.exists("encrypted_" + file_name + ".txt")):
        os.remove(os.path.abspath("encrypted_" + file_name + ".txt"))
    
    target = open("encrypted_" + file_name + ".txt", "a")

    read = file.readlines()
    write = [translate_text(code, nums, file_ext) + "\n"]

    for line in read:
        write.append(translate_text(code, nums, line))
    
    for line in write:
        target.write(line)
    
    file.close()
    target.close()

#Key.create_code("test_keys", 3, 3)
#Key.create_number_key("test_nums", Key.create_character_key(20, 20), Key.create_character_key(20, 20))
translate_file(
    os.path.abspath("test_keys.json"),
    os.path.abspath("test_nums.json"),
    os.path.abspath("Sample.txt")
)
translate_file(
    os.path.abspath("test_keys.json"),
    os.path.abspath("test_nums.json"),
    os.path.abspath("test_keys.json")
)
translate_file(
    os.path.abspath("test_keys.json"),
    os.path.abspath("test_nums.json"),
    os.path.abspath("test_nums.json")
)