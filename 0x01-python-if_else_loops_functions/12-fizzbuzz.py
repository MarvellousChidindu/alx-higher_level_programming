#!/usr/bin/python3
def fizzbuzz():
    for nums in range(1, 101):
        if nums % 3 == 0 and nums % 5 == 0:
            print(f"FizzBuzz", end=' ')
        elif nums % 3 == 0:
            print(f"Fizz", end=' ')
        elif nums % 5 == 0:
            print(f"Buzz", end=' ')
        else:
            print(nums, end=' ')
