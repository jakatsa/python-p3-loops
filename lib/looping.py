#!/usr/bin/env python3
def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1

# Call the function
happy_new_year()
# Print "Happy New Year!" on a new line
print('Happy New Year!\n')

        
  

def square_integers(int_list):
    return [num ** 2 for num in int_list]


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def fizzbuzz_printer():
    for num in range(1, 101):
        print(fizzbuzz(num))

# Call the function
fizzbuzz_printer()


