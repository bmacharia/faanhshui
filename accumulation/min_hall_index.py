"""
  Now you know how many guests are in your hall. However, you must tell Master Qu which hall you’ll join. The halls are numbered from 0 to N-1, where N is the total number of halls.

  Write a function that returns the index of the hall you should join—the one with the minimum number of guests. If multiple halls have the same minimum number, return the one with the smallest index.


"""

class Solution:
    def min_hall_index(self, halls):
        min_value = halls[0]
        min_index = 0
        for i in range(len(halls)):
            if halls[i] < min_value:
                min_value = halls[i]
                min_index = i
        return min_index
    
s = Solution()
print(s.min_hall_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
