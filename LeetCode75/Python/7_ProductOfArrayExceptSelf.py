class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prod = {}

        for index, num in enumerate(nums):
            prod[index] = num
        
        new_prod = {}
        

sol = Solution()
sol.productExceptSelf([-1,1,0,-3,3])