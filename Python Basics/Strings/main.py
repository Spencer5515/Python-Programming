print("===== STRINGS =====\n")

i = 1
temp_char = "r"
temp_repl = "Elephant"
phrase = "Giraffe \\ Academy"
print(phrase + " is cool")

print(phrase.lower()) # convert to lowercase
print(phrase.upper()) # covert to uppercase
print()
print(phrase.isupper()) # returns bool if is entirely uppercase
                            # str(<data>) converts to string
print("Phrase Length: " + str(len(phrase))) # gets Char length of 'phrase'

print("Elem at index " + str(i) + ": " + phrase[i]) # gets elem at 1st index of string
print("Index of Char " + temp_char + ": " + str(phrase.index(temp_char))) # gets index of char
print(phrase.replace("Giraffe", temp_repl)) # replace function


