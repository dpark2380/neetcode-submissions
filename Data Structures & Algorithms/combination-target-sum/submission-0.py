class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.ans = []
        self.nums = nums

        curarray = []
        self.dfs(0, 0, curarray)

        return self.ans
    
    def dfs(self, i, cursum, curarray):
        if cursum == self.target:
            self.ans.append(curarray.copy())
            return
        
        if cursum > self.target or i >= len(self.nums):
            return
        
        curnum = self.nums[i]

        if cursum + curnum <= self.target:
            curarray.append(curnum)
            self.dfs(i, cursum + curnum, curarray)
            # Removing the last added element to try other combinations.
            curarray.pop()
        
        # This branch runs everytime.
        self.dfs(i + 1, cursum, curarray)



