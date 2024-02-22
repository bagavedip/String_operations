# Using str.replace()
string = 'Geeks123For123Geeks'
result = string.replace('123', '')
print(result)
# Using translate()
strg = 'Geeks123For123Geeks'
res = strg.translate({ord(i): None for i in "123"})
print(res)
# Using Native Method
test_str = "GeeksForGeeks"

# Removing char at pos 3
new_str = ""

for i in range(len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]

# Printing string after removal
print("The string after removal of i'th character : " + new_str)
# Using slice + concatenation
strg = 'Geeks123For123Geeks'
result = strg[:5] + strg[8:11] + strg[-5:]
print(result)
# Using str.join()
strg = 'Geeks123For123Geeks'
result = strg.strip("123").join('')
print(result)
