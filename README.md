# Count List Items - Recursive Implementation

This Python project showcases a recursive function, count_items, that counts the number of items in a list. The function uses a divide-and-conquer approach, reducing the problem's size in each recursive call.

# Function

Here's the core function of the project:

```python
def count_items(arr: list, left: int = 0, right: int = None) -> int:
    if right is None:
        right = len(arr)

    if left >= right:
        return 0
    if (right - left) == 1:
        return 1

    mid = (left + right) // 2
    return count_items(arr, left, mid) + count_items(arr, mid, right)
```

# Usage

To use the function, call it with a list as the argument:

```python
items = ['a', 'b', 'c', 'd', 'e']
print(count_items(items))  # Outputs: 5
```

# Limitations

This implementation uses recursion and Python has a limit to the recursion depth (typically 1000). Therefore, this function may result in a RecursionError for larger lists.

For lists close to or exceeding this limit, consider using an iterative approach or the built-in len() function in Python.

# Contributing

Fork this project and add your own features or improvements!