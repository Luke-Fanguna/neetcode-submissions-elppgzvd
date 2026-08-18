class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []
        combo = []
        def backtrack(i, n):
            # If we correctly find a combo
            if n == target:
                combinations.append(combo[::])
                return
            # If we have checked every candidate and it doesn't work, stop.
            # OR if number is too large, stop.
            elif i >= len(candidates) or n > target:
                return

            # include
            combo.append(candidates[i])
            backtrack(i+1, n + candidates[i])

            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            # exclude
            combo.pop()
            backtrack(i+1, n)
        
        backtrack(0, 0)
        return combinations
