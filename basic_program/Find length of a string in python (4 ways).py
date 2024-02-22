# program to find length of string using len() method
example = "Dipika"
result = len(example)
print(f"length of string is {result}")

# program to find length of string using for loop
sub_string = "Dhiraj"
count = 0
for i in sub_string:
    count += 1

print(f"length of sub_string is {count}")

# program to find length of string using sum method

sub_string = " Dipika"
result = sum(1 for i in sub_string)
print(result)

# program to find length of string using enumerate
sun_string = "hello"
counter = 0
for i, v in enumerate(sun_string):
    counter += 1
print(counter)
