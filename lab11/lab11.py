# -*- coding: utf-8 -*-
"""lab11

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oLgs0o4QyqXOx7XXtnjvkzm24-2-zhpz
"""

n = int(input())
while n >= 0 :
  if n % 2 == 0 :
    print(n, "is even number")
  else :
    print(n, "is odd number")
  n = int(input())

n = int(input())
for i in range(n + 1) :
  for j in range(i) :
    print(i, " ", end = "")
  print()

import numpy as np

arr = np.array([[8, 5, 6], [4, 7, 1], [6, 3, 2]])
print(arr[0: , : 2])