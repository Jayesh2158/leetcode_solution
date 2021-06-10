from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map=Counter(nums) 
        value=list(map.values())
        for i in value:
            if i>1:  
                return "true"
        else:
            print('false')
