# reverse words in a given string in python using spit, join method.
string = " geeks quiz practice code"
result = string.split(" ")[::-1]
start = " "
results = start.join(result)
print(results)

# reverse words in a given string in python using split, join reversed method.
string = "geeks quiz practice code"
result = string.split(' ')
remo = ' '.join(reversed(result))
print(remo)
