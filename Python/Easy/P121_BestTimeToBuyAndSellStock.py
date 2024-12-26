# from typing import List
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        
#         print(int(float('-inf')))
#         # [7,1,5,3,6,4] 
#         max_profit = float('-inf')
#         highest_price = max(prices)
        
#         lenP = len(prices)
#         for i in range(lenP-1):
#             for j in range(i+1, lenP):
#                 if (prices[i] < highest_price):
#                     profit = prices[j] - prices[i]
#                     max_profit = max(profit, max_profit)
                
#         if(max_profit == -1):
#             return 0      
#         return max_profit
    
# sol = Solution()
# # print(sol.maxProfit([7,1,5,3,6,4]))
# print(sol.maxProfit([7,6,4,3,1]))

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price
            
            if profit > max_profit:
                max_profit = profit
        return max_profit
    
sol = Solution()
print(sol.maxProfit([7,6,4,3,1]))