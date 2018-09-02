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
    if i + 1 < len(s):
        if s[i] > s[i + 1]:
            temp = ''

print("Longest substring in alphabetical order is: {}".format(result))