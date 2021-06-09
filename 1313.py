nums=[1,2,3,4]
res=[]
i=0
while i<len(nums):
	for j in range(nums[i]):
		res.append(nums[i+1])
	i+=2

print(res)
		
