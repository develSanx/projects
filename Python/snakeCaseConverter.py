str = input()
word = ''
for char in str:
    if char.isupper():
        word += '_' + char.lower()
    if char.islower():
        word += char
print(word)
