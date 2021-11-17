nums= [int(nums) for nums in input("Enter multiple value: ").split(",")]
print("Number of list is: ", nums)

target=int(input("Enter the sum :-"))
size=int(input("Enter the number of element to Enter :- "))

for i in range(len(nums)): 
        Sum=nums[i]+nums[i+1]
        if Sum==target:
            print("[",i,",",i+1,"]")
        else:
            pass


