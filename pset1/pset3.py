"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

# Prints number of times of string 'bob' occurs in string s
s = 'abcbde'

result = temp = ''
for i in range(len(s)):
    # Appends the current character into temp
    temp += s[i]

    # temp length > result length, new result
    if len(temp) > len(result):
        result = temp

    # If next character is smaller, break the chain/clear temp
    # Last character is guaranteed, no need to consider if it is smaller or not
    if i + 1 < len(s):
        if s[i] > s[i + 1]:
            temp = ''

print("Longest substring in alphabetical order is: {}".format(result))