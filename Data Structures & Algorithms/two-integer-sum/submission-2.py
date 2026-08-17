class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for x in range(len(nums)):
            number = target - nums[x]

            if number in m:
                return [m[number], x]

            m[nums[x]] = x