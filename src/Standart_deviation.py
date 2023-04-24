#!/usr/bin/env python3

import re 
from mathlib import *

input_numbers = ""
while True:
    try:
        line = input()
    except EOFError:
        break
    input_numbers += line.strip() + " "

numbers = re.split('\s+', input_numbers.strip())

if len(numbers) < 2:
    print("nizky pocet cisiel")
    exit()

numbers = [float(number) for number in numbers]

############################# mean if numbers

lenght_of_numbers_list = len(numbers)

sum_of_numbers = 0
for num in numbers:
        sum_of_numbers = add(sum_of_numbers, num)

mean_of_numbers =  div(sum_of_numbers, lenght_of_numbers_list)
print ("mean of numbers is", mean_of_numbers)

############################# standart deviation
##### sum (xi- x_priemer)pwr 2
sum_num_sub_mean = 0
for x in numbers: 
    sum_num_sub_mean = add(sum_num_sub_mean, pwr(sub(x, mean_of_numbers), 2))

##### N - 1 
N_sub_1 = sub(lenght_of_numbers_list, 1)    

Standart_deviation = sqrt(div(sum_num_sub_mean, N_sub_1))

print ("Standart deviation of the numbers is ", Standart_deviation)