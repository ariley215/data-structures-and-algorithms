# Challenge Title

Sum rows of a matrix

## Whiteboard Process

![Challenge 4 Whiteboard](python/docs/matrix-sum/CodeChallenge4_2024-01-12_14-30-57.png)

## Approach & Efficiency

I found the length of the array. Then used a nested for loop inside a while loop to iterate over the rows in the matrix and then iterate over the elements in each row. The elements are added together and that sum is appened to a new array. This repeats until all og the rows have been summed. Then the new array with row totals as elements is returned.

## Solution

```python
def sum_rows(matrix):
    matrix_length = len(matrix)
    sums_array = []
    row_index = 0
    while row_index < matrix_length:
        current_array = matrix[row_index]
        array_sum = 0
        for element in current_array:
            array_sum += element
        sums_array.append(array_sum)
        row_index += 1
    return sums_array
```
