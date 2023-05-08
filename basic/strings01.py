# src: https://www.w3schools.com/python/python_strings.asp
# src: https://www.w3schools.com/python/python_ref_glossary.asp
# stings practices with print() function
# Compare with C programing language:character, string?!
# What's the difference?

strings = "Hello World!"

print("Original strings:", strings)
print("Length of strings is:", len(strings))
print("Character at index 0 in strings:", strings[0])
# upper()
# lower()
# print(strings.upper)
# <built-in method upper of str object at 0x7f7c1c521ab0>
up = strings.upper()
print("Using upper method:", up)
low = up.lower()
print("Using lower method:", low)