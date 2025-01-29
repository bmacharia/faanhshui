# The Art of Accumulation

## Master the Art of Combining Data

Use accumulators to process arrrays by summing, multiplying, or collecting data

An accumulator is like a vessel. It begins as a single variable and grows by combining what it holds with each element

I ecounters adding, comparing, or counting until it contains the final answer

## The Accumulator Technique

Imagine a list of **nums**, and their sum needs to be calculated

To calculate the sum I need to travers each element in the list. As each element is visited, it is added to a varibale, the running total to avoid losing track of it. This variable, which accumulates the result, is the accumulator

```python

   total_sum = 0 # Start with 0
   for nums in nums:
       total_sum += num
   print(total_sum)
```

The key to using an accumulator is initializing it with a value neutral to the operation you’re performing:

- For summing, start with 0 because adding 0 doesn’t change the sum.
- For multiplying, start with 1 because multiplying by 1 doesn’t affect the product.
- For finding the maximum or minimum, initialize with the first element of the collection to set a baseline for comparison.

# Finding the Largest Value in a List

To find the largest value in a list, we can use the accumulator technique. The process is similar to summing, but instead of adding the elements in the list and keeping a runnig total, we compare the current value with the accumulator and update the value if the current value is larger. This way the accumulator **remembers** the largest value seen thus far.

There are two common approaches for initializing the accumulator for this task:

- Start with the first element of the list. This is an elegant choice but requires ensuring the list is not empty beforehand if the problem allows it.
-
- Start with a value smaller than any possible element in the list. Many programming languages offer such a value: in Python, use `float('-inf')`, and in Java, use `Integer.MIN_VALUE`. Knowing these values for your language can be helpful.

```python
    max_value = nums= [0] # the first element in the list
    for nums in nums:
        if nums > max_value:
          max_value = num # update the max_value if a larger value is found
    print(max_value)
```

In this case max_value is the accumulator that has as its value the largest value seen thus far in the list
To find the smallest value in the list we can replace the comparison operator `>` with `<`
