# Challenge Title

Insert and shift an array at the middle index

## Whiteboard Process
<!-- Embedded whiteboard image -->
![Challenge 2 Whiteboard](/python/docs/array-insert-shift/CodeChallenge2_2024-01-10_15-25-56.png)

## Approach & Efficiency

I took the input value and turned it into an array. Then the input array is iterated over. The elements that have an index that is less than the middle index go into a new array. The elments that have an index higher than the middle index are added to a differnt array. Then the arrays are concatenated into a new array so that the array containing the input value is in the middle or to the right of the previous middle element.

Time: 0(n)
Time to iterate through the array is proportional to the length of the array

Space: O(n)
More space is needed to store the split arrays

## Solution
<!-- Show how to run your code, and examples of it in action -->
```python
def shift_array(input_array, input_value):
    input_value_array = [input_value]
    middle_index = len(input_array) // 2
    first_half = []
    second_half = []

    for i, element in enumerate(input_array):
        if i < middle_index:
            first_half.append(element)
        else:
            second_half.append(element)

    new_array = first_half + input_value_array + second_half

    return new_array

# Example usage:

input_array_example = [1, 2, 3, 4, 5]
input_value_example = 100
result_example = shift_array(input_array_example, input_value_example)
print(result_example)
```

## Tests

```python
def test_shift_array():
    # Happy Path - Expected outcome
    input_array1 = [1, 2, 3, 4, 5]
    input_value1 = 100
    result1 = shift_array(input_array1, input_value1)
    assert result1 == [1, 2, 100, 3, 4, 5], f"Test Case 1 Failed: {result1}"

    # Expected Failure
    # For example, if the function is not implemented correctly, this test might fail
    input_array2 = [10, 20, 30, 40, 50, 60]
    input_value2 = 999
    result2 = shift_array(input_array2, input_value2)
    assert result2 == [10, 20, 30, 999, 40, 50], f"Test Case 2 Failed: {result2}"

    # Edge Case (Empty array)
    input_array3 = []
    input_value3 = 999
    result3 = shift_array(input_array3, input_value3)
    assert result3 == [999], f"Test Case 3 Failed: {result3}"

    # Edge Case (Array with one element)
    input_array4 = [7]
    input_value4 = 777
    result4 = shift_array(input_array4, input_value4)
    assert result4 == [7, 777], f"Test Case 4 Failed: {result4}"

    print("All test cases passed successfully!")

# Run the test cases

test_shift_array()

```
