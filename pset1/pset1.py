"""
Problem 1
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""

# Vowel
vowel = ['a', 'e', 'i', 'o', 'u']

# Counting the number of vowels
num = 0

# The main loop
for i in range(len(vowel)):
    num += s.count(vowel[i])

# Print the result
print("Number of vowels: {}".format(num))

