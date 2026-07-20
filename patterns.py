# operator precedence mai PEMDAS rule ko follow kiya jata hai

# n = 5
#
# for i in range(1, n):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

# Right aligned triangle

# n = 5

# for i in range(1, n):
#     for j in range(n - i):
#         print(' ', end='')
#     for k in range(i):
#         print("*", end='')
#     print()

"""
Hollow square with center star -

* * * * *
*       *
*   *   *
*       *
* * * * *

"""
# n = 5
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == 1 or i == n or j == 1 or j == n or (i == 3 and j == 3):
#             print("*", end=" ")
#         else:
#             print(' ', end=" ")
#     print()

"""
Pyramid -

    *
   ***
  *****
 *******
*********

"""

# n = 5
#
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end="")
#     for j in range(2 * i + 1):
#         print("*", end="")
#     print()

"""
Simple circle pattern - 

        *********
     ***************
   *******************
  *********************
 ***********************
 ***********************
 ***********************
  *********************
   *******************
     ***************
        *********
"""


radius = 8

for i in range(2 * radius + 1):
    for j in range(2 * radius + 1):
        x = i - radius
        y = j - radius

        distance = x*x + y*y

        if radius*radius - radius <= distance <= radius*radius + radius:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()




















