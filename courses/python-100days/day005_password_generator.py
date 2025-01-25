import random


letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
numbers = [str(i) for i in range(10)]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']

length = int(input("How long do you want your password to be? "))

count_numbers = int(input("How many numbers do you want to include? "))
count_symbols = int(input("How many symbols do you want to include? "))

password_chars = []
for i in range(0, length - count_numbers - count_symbols):
    password_chars += random.choice(letters)
for i in range(0, count_numbers):
    password_chars += random.choice(numbers)
for i in range(0, count_symbols):
    password_chars += random.choice(symbols)


print(f"Simple password: {''.join(password_chars)}")
random.shuffle(password_chars)
print(f"Complex password: {''.join(password_chars)}")
