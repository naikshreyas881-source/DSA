# Extraction of Digits from an Integer
num=5870
while num>0:
    last_digit=num%10
    print(last_digit)
    num=num//10
print(num%10)
# output= 5 8 7 0


#Count the number of Digits in an Integer
 num=75443467
 count=0

 while num>0:
     count+=1
     num=num//10
    print(count)
# output=8

#Check if a number is Palindrome or Not
num = 153
n = num
rev = 0

while num > 0:
    ld = num % 10
    rev = rev * 10 + ld
    num = num // 10

if rev == n:
    print("Palindrome")
else:
    print("Not a Palindrome")
    #output= not a palindrome 
