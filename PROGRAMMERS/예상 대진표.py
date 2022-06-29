keyboard = ["a", "b", "c"], ["a", "e", "f"]

key_str = ""
for i in range(len(keyboard)):
    for j in range(len(keyboard[i])):
        key_str += keyboard[i][j]

print(key_str.index('k'))

print(key_str)