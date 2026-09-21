class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        # Using property of XOR: any number bit XORed with itself will be 0
        # any number XORed with itself will be 0. 
        # Since numbers appear either once or twice, all numbers appearing twice 
        # will be 0, and any number appearing once will survive.
        for num in nums:
            ans ^= num
        return ans