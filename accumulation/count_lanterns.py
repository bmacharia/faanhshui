"""
  Given a list representing lanterns where 1 indicates the lantern is lit and -1 indicates the lantern is unlit, write a function to count how many are lit using an accumulator.
  Example: For [1, -1, 1, 1, -1], the function should return 3.  

"""

class Solution:
  def count_lit_lanterns(self, lanterns):
    count = 0
    for lantern in lanterns:
      if lantern == 1:
        count += 1
    return count
  
s = Solution()
print(s.count_lit_lanterns([1, -1, 1, 1, -1])) # 3