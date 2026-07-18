""""
List
"""

"""
second largest element - 
"""

# def second_largest_element(lst):
#     first = float('-inf')
#     second = float('-inf')
#
#     for num in lst:
#         if num > first:
#             second = first
#             first = num
#
#         elif num > second and num != first:
#             second = num
#     return second
#
# print(second_largest_element([10, 20, 5, 8, 15]))

"""
remove duplicates - 
"""

# def remove_duplicates(lst):
#     seen = set()
#     result = []
#     for item in lst:
#         if item not in seen:
#             seen.add(item)
#             lst.append(item)
#
#     return lst
#
# print(remove_duplicates([1, 2, 2, 3, 1, 4, 5, 4]))

"""
rotate list
"""
#
# def rotate_list(lst, k):
#     n = len(lst)
#     k = k % n
#
#     for i in range(k):
#         value = lst.pop()
#         lst.insert(0, value)
#
#     return lst
#
# print(rotate_list([1, 2, 3, 4, 5], 2))








