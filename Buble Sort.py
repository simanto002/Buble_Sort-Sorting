print("Hey User")
print("Welcome")
def sort(nums):
  for i in range (len(nums)-1,0,-1):
    for j in range(i):
      if nums[j]>nums[j+1]:
        tem=nums[j]
        nums[j]=nums[j+1]
        nums[j+1]=tem
      print(nums)
nums=[4,41,24,25,26,87,14,58,32]
sort(nums)
print(nums)
