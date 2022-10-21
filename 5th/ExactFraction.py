from fractions import Fraction
s = input().replace(" ", '')

oper = ['(', ')', '+', '-', '*', '/', '%']
new_s = ""
digit = False
for i in range(len(s)):
    if s[i] in oper:
        if digit:
            new_s += f"Fraction('{s[start:i]}')"
            digit = False
        new_s += s[i]
    elif not digit:
        digit = True
        start = i
if digit:
    new_s += f"Fraction('{s[start:]}')"
print(eval(new_s))
