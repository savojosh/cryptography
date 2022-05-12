import os
import json
import Key

def untranslate_text(code, nums, encryptedText):
    untranslated = ""
    translated = encryptedText
    translation_num = 0

    nums_file = open(nums, "r")
    nums_dictionary = json.load(nums_file)
    nums_source = nums_dictionary.get("nums")
    nums_file.close()

    keys_file = open(code, "r")
    keys_dictionary = json.load(keys_file)
    keys_list = list(keys_dictionary.items())
    keys_file.close()

    while(len(translated) > 0):
        char = ""
        translated_key = False

        for key in keys_list:
            if(translated.find(key[1]) == 0):
                char = Key.translate_key_to_char(key[0], nums_source[translation_num])
                untranslated += char
                translated = translated[len(key[1]):]
                if(translation_num >= len(nums_source) - 1):
                    translation_num = 0
                else:
                    translation_num += 1
                translated_key = True
                break
    
        if(not translated_key):
            char = translated[:1]
            translated = translated[1:]
            untranslated += char

    return(untranslated)

def untranslate_file(code, nums, absoluteFilePath):
    file = open(absoluteFilePath, "r")
    encrypted_lines = file.readlines()
    decrypted_lines = []

    path = list(os.path.split(absoluteFilePath))
    fileExt = untranslate_text(code, nums, encrypted_lines[0])
    path[1] = str(path[1])[10:len(path[1]) - 4] + fileExt

    for i in range(len(encrypted_lines) - 1):
        decrypted_lines.append(untranslate_text(code, nums, encrypted_lines[i + 1]))

    file.close()
    file = open(absoluteFilePath, "w")
    file.writelines(decrypted_lines)
    file.close()

    os.rename(
        absoluteFilePath,
        path[0] + "e" + path[1][:len(path[1]) - 1]
    )

#line = "hxmp~#l,FmoaciD"
#print(untranslate_text("test_keys.json", "test_nums.json", line))
untranslate_file("test_keys.json", "test_nums.json", "encrypted_Sample.txt")