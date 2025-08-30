# Example Usage of AI Debugging Assistant Prompt

## Sample Student Code (with bugs)

```python
def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += i  # Bug: should be total += numbers[i]
    average = total / len(numbers)
    return average

# Test the function
my_numbers = [10, 20, 30, 40]
result = calculate_average(my_numbers)
print(f"The average is: {result}")
```

**Expected Output:** The average is: 25.0
**Actual Output:** The average is: 1.5

## How to Use the Prompt

1. Replace `{{STUDENT_CODE}}` with the buggy code above
2. Replace `{{EXPECTED_OUTPUT_OR_BEHAVIOR}}` with "Should calculate and return the average of a list of numbers"
3. Replace `{{STUDENT_LEVEL}}` with "BEGINNER"

## Expected AI Response (following the prompt)

```xml
<analysis>
I can see you're trying to create a function that calculates the average of a list of numbers. Your overall structure is good - you're initializing a total, using a loop to process the numbers, and then dividing by the length. However, the result you're getting (1.5) is quite different from what you'd expect for the average of [10, 20, 30, 40].
</analysis>

<questions>
1. When you loop through your numbers list, what exactly are you adding to the total variable?
2. What do you think the variable 'i' represents in your loop?
3. If you wanted to access the actual numbers in your list, how would you do that using the index 'i'?
</questions>

<hints>
Try adding a print statement inside your loop to see what values are actually being added to your total. Print both 'i' and what you think should be the actual number from your list. This will help you see the difference between the index position and the actual values.
</hints>

<encouragement>
You're very close! Your logic for calculating an average is correct, and your loop structure is perfect. This is a common mistake that many programmers make when starting out. Once you see what's happening in that loop, you'll have it figured out!
</encouragement>
```

## Why This Response Works

1. **No Direct Solution**: Doesn't say "change `i` to `numbers[i]`"
2. **Guided Discovery**: Questions lead the student to understand index vs. value
3. **Debugging Technique**: Suggests print statements for investigation
4. **Appropriate Level**: Uses simple language for a beginner
5. **Encouraging**: Acknowledges what they did right and normalizes the mistake

## Alternative Response for Advanced Student

If the same code came from an advanced student, the response might be:

```xml
<analysis>
Your function structure follows good practices, but there's a logical error in your accumulation step that's causing incorrect results. The discrepancy between expected and actual output suggests an issue with what values you're summing.
</analysis>

<questions>
1. What's the difference between iterating over indices versus iterating over values?
2. Could you rewrite this function using a more Pythonic approach?
3. What would happen if you tested this with edge cases like an empty list?
</questions>

<hints>
Consider using Python's built-in functions or direct iteration. Also, think about error handling - what should happen if the list is empty? Your current implementation would raise a ZeroDivisionError.
</hints>

<encouragement>
This is a good opportunity to explore different iteration patterns in Python and consider edge cases that make code more robust!
</encouragement>
```

This demonstrates how the same prompt adapts to different student levels while maintaining the core principle of guided discovery.
