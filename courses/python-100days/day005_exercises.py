
# FizzBuzz
for n in range(0, 100):
    fizzed_or_buzzed = False
    if n % 3 == 0:
        print("Fizz", end="")
        fizzed_or_buzzed = True
    if n % 5 == 0:
        print("Buzz", end="")
        fizzed_or_buzzed = True
    if not fizzed_or_buzzed:
        print(n, end="")

    print("")


# Array concat
array1 = ['a', 'b', 'c', 'd', 'e']
array2 = ['f', 'g', 'h', 'i', 'j']

concatenated_array = array1 + array2
print(concatenated_array)

# Random
import random
print(random.randint(1, 10))

random.shuffle(concatenated_array)
print(concatenated_array)

# String to array to strint
string_to_convert = "hello world"
converted_array = list(string_to_convert)
random.shuffle(converted_array)
print(converted_array)
back_to_string = "".join(converted_array)
print(back_to_string)