#!/usr/bin/python3
def fizzbuzz():
    for i in range(1,101):
        print([i,"Buzz","Fizz","Fizzbuzz"][2*(i%3==0) + (i%5==0)], end=' ')
