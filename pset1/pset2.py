# Prints number of times of string 'bob' occurs in string s
# Comment this line below if not using it
s = 'azcbobobobobobobobobobobobegghakl'

word = 'bob'

result = 0
for i in range(len(s) - len(word) + 1):
    if word in s[i:i + len(word)]:
        result += 1

print("Number of times {} occurs is: {}".format(word, result))

