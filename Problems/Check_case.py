# Write a program that takes a character as input and prints either 1, 0 or -1 according to the following rules.
# 1, if the character is an uppercase alphabet (A - Z)
# 0, if the character is a lowercase alphabet (a - z)
# -1, if the character is not an alphabet



char = input()
if ord(char)>=65 and ord(char)<=90:
    print(1)
elif ord(char)>=97 and ord(char)<=122:
    print(0)
else:
    print(-1)
