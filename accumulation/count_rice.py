"""
After noticing the focused determination of the students studying their scrolls, Master Qu, the Quartermaster, approaches with a knowing smile. "Ah, eager minds at work!" he says warmly. "Perhaps one of you can assist me. To prepare for next month’s supplies, I need to calculate the total number of rice bags stored in the temple’s storage units."

Write a function that returns the total number of bags of rice given a list of bags per storage unit.
Note: Do not use built-in summing functions. Use an accumulator and a loop instead.

"""

"""
The methon count_rice takes in a list of rice bags and returns the total number of rice bags stored in the temple's storage units. The method uses an accumulator to keep track of the total number of rice bags. The method iterates through the list of rice bags and adds each bag to the accumulator. The method then returns the total number of rice bags.
"""

class Solution:
    def count_rice(self, rice_bags):
        total_bags = 0
        for bags in rice_bags:
            total_bags += bags  
        return total_bags

Solution = Solution()
rice_bags = [10, 20, 30, 40, 50]
print(Solution.count_rice(rice_bags)) # 150
