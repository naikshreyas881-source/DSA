# Extraction of Digits from an Integer
num=5870
while num>0:
    last_digit=num%10
    print(last_digit)
    num=num//10
print(num%10)
# output=
0
7
8
5
0
