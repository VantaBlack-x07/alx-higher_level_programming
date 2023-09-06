#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        if a % 15 == 0:
            print("FizzBuzz".format(), end=" ")
            continue
        elif a % 3 == 0:
            print("Fizz".format(), end=" ")
            continue
        elif a % 5 == 0:
            print("Buzz".format(), end=" ")
            continue
        else:
            print(a, end=" ")
