#!/usr/bin/env python3
def change(b):
    global a
    a = 90
    print(a)
a = 9
print("Before the function call ", a)
print("Inside change function", end = '')
change(a)
print("After the function call ", a)
