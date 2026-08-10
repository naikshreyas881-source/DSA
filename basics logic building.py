#store the frequency in dictonary
nums=[5,6,7,7,1,9,111,1,1,5,1,1]
freq_map = {}

for i in range(len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map)


#Print the count of each element in the same order as it appears in m
# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]
n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
for num in m:
    count=0
    for x in n:
        if x==num:
            count+=1
    print(count)

#Print the count of each element in the same order as it appears in m
# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]  using hash method 
n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
hash_list=[0]*11
for num in n:
    hash_list[num]+=1
for num in m:
    if num<1 or num>10:
       print(0)
    else:
       print(hash_list[num])

# Print monstor 4 times
def func(count):
    if count == 4:
        return

    print("monster")
    func(count + 1)

func(0)

# Print monstor 4 times(backtraking)
def func(count):
    if count == 4:
        return

    func(count + 1)
    print("monstor")

func(0)

# print x in n times
def func(x,n):
    if n == 0:
        return
    print(x)
    func(x,n-1)
func(1,8)


# print 1 to n using recursion
def func (i,n):
    if i>n:
        return
    print(i)
    func(i+1,n)
func(1,6)

# print n to 1 (backtraking)
def func (i,n):
    if i>n:
        return
    func(i + 1, n)
    print(i)
func(1,6)

# print 1toN
def func(n):
    if n == 0:
        return
    func(n-1)
    print(n)
func(6)

# factorial of the number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
factorial(5)
print(factorial(5))

#Given a string s, check if it is a palindrome or not. A palindrome is a word, phrase, or sequence that reads the same backward as forward.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def func(left, right):
            if left >= right:
                return True

            if s[left] != s[right]:
                return False

            return func(left + 1, right - 1)

        return func(0, len(s) - 1)
#The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
class Solution:
    def fib(self, n: int) -> int:
        def func(n):
            if n ==0 or n==1:
                return n
            return func(n-1)+func(n-2)
        answer=func(n)
        return answer    
