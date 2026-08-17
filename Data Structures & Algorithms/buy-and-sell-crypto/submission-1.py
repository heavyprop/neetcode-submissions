class Solution:
    # so we are just calculating the max profit by subtracking left to right:
    # essentially doing 2 checks:
    # -- is going 1 right making the profit go up
    # -- is going 1 right a cheaper buying price 
    # keep doing that right is last item
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        
        for _ in range(len(prices)):
            
            if right < len(prices):
                profit = prices[right] - prices[left]
            else:
                break
            
            if profit > max_profit:
                max_profit = profit
            
            if prices[right] < prices[left]:
                left = right

            right += 1

        return max_profit