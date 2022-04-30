import os
import json
import Key

def translate(code, nums, text):
    translation = ""
    translation_num = 0

    for character in text:
        if(character == " "):
            translation += character
        else:
            translation += Key.translate_num_to_key(code, character, nums[translation_num])
            translation_num += 1
        
        if(translation_num >= len(nums)):
            translation_num = 0
    
    return translation

Key.create_code("test", 3, 3)
word_1 = Key.create_character_key(20, 20)
word_2 = Key.create_character_key(20, 20)
print(word_1)
print(word_2)
num_key = Key.create_number_key(word_1, word_2)
print(num_key)
print(translate("test.json", num_key, "Welcome to Joshua's Wall of Text! Here, we will see nothing except text."))