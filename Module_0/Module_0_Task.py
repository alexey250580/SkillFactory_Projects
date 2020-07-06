#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Задача по определению загаданного числа

import numpy as np
number = np.random.randint(1,101)
print('Загадано число от 1 до 100')

#Определение начальных значений используемых переменных

count = 1
min_number = 1
max_number = 100

#Функция для определения среднего значения интервала, в котором осуществляется поиск загаданного числа

def average(min_number, max_number):
    predict = min_number + (max_number - min_number) // 2
    return predict

#Цикл для поиска загаданного числа и подсчета количества попыток

while number != average(min_number, max_number):
    count += 1
    if number in range(min_number, average(min_number, max_number)-1):
        max_number = average(min_number, max_number)
        average(min_number, max_number)
    elif number in range(average(min_number, max_number)+1, max_number):
        min_number = average(min_number, max_number)
        average(min_number, max_number)
        
print('Загаданное число равняется', number,', а угадано оно было за', count, 'попыток.')

