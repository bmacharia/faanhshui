"""
As you head to the guest wing, Master Qu explains, "We keep our guest halls balanced. Newcomers join the hall with the fewest guests."

Write a function that returns the number of guests in the hall you’ll join - the hall with the fewest guests, given a list of guest counts per hall.
Note: Do not use built-in min function; use an accumulator and a loop to find the minimum.

max_value = nums= [0] # the first element in the list
    for nums in nums:
        if nums > max_value:
          max_value = num # update the max_value if a larger value is found
    print(max_value)



"""
class Solution:
    def min_hall(self, halls):
        min_value = halls[0] # the first element in the list
        for hall in halls:
            if hall < min_value:
                min_value = hall # update the min_value if a smaller value is found
        return min_value


