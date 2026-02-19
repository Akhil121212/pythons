#To add two numbers
# 1)Predefined 
'''
num1 = 30
num2 = 40
sum = num1+num2
print("The sum of given two numbers is:",sum)

#2)with inputs

num1 = float(input("Enter the first number:"))
num2 = float(input("ENter the second number:"))

sum = num1+num2
print("The sum of the provided numbers is :",sum)
'''
#Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
#Return the array in the form [x1,y1,x2,y2,...,xn,yn].
'''
class Solution:
    def shuffle(self, nums, n):
        ans = []

        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])

        return ans
        '''
         