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
