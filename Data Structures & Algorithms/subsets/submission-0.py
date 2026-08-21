class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # saving the result
        res = []

        # saving the subset
        subset = []

        # recursive call
        def dfs(i):
            # if the index is greater than the number of items
            if i >= len(nums):
                # then append the copy of subset
                res.append(subset.copy())
                # then return back to the previous dfs call
                return

            # subset append index i number
            subset.append(nums[i])

            # call dfs with new index
            dfs(i + 1)

            # pop the last number
            subset.pop()

            # try again with popped
            dfs(i + 1)

        dfs(0)
        return res
