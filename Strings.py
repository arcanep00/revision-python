# number pattern

# n = 5
# for i in range(1, n):
#     for j in range(1, i + 1):
#         print(j , end=" ")
#     print()
#
#

# s = "Python"
#
# s = "J" + s[1:]
#
# print(s)
#


# s = "I like JAVA"
# print(s.replace("JAVA", "PYTHON"))

# s = "Python programming"
#
# print(s.find("pro"))
# print(s.count("o"))

# s = "Python is easy"
#
# print(s.split())
#

"""
Problem 1: Reverse words
"""

# def reverse_words(s):
#     result = ""
#     words = s.split()
#
#     for i in range(len(words) - 1, -1, -1):
#         result += words[i]
#
#         if i != 0:
#             result += " "
#
#     return result
#
# print(reverse_words("Python is awesome"))

"""
Question 2: First Non-Repeating Character
"""

# def first_non_repeating_character(s):
#     dict = {}
#     for ch in s:
#         if ch in dict:
#             dict[ch] += 1
#         else:
#             dict[ch] = 1
#
#     for ch in dict:
#         if dict[ch] == 1:
#             return ch
#     return None
#
# print(first_non_repeating_character("aabbccdde"))

# Question 3: String Compression

# def compress_string(s):
#     if not s:
#         return ""
#
#     result = ""
#     count = 1
#
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             result += s[i - 1] + str(count)
#             count = 1
#
#     result += s[-1] + str(count)
#     return result
#
# print(compress_string("aaabbcccdaa"))


























