""""
List
"""

def second_largest_element(lst):
    first = float('-inf')
    second = float('-inf')

    for num in lst:
        if num > first:
            second = first
            first = num

        elif num > second and num != first:
            second = num
    return second

print(second_largest_element([10, 20, 5, 8, 15]))


