# operator precedence mai PEMDAS rule ko follow kiya jata hai

# n = 5
#
# for i in range(1, n):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()


n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(i):
        print("*", end='')
    print()
