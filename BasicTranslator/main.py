# Basic Translator
print("=== Basic Translator ===\n")

# Giraffe Language
# vowels -> g
# dog -> dgg

def translate(phrase):
    translation = ""
    for letter in phrase:  # for-each loop
        if letter.lower() in "aeiou":  # checks if 'letter' is inside string
            if letter.isupper():  # if
                translation += "G"
            else:  # else
                translation += "g"
        else:  # else
            translation += letter
    return translation


print(translate(input("Enter a phrase: ")))  # prints, translation, of user I/O
