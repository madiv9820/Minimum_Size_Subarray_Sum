# Brute Force 🐢

[⬅ Back to README](../README.md)

## Intuition 💡

The simplest way to solve the problem is to try every possible subarray.
For each starting index, extend the subarray one step at a time and keep adding values.
As soon as the running sum becomes at least `target`, record that length.

Because all numbers are positive, extending the same subarray further would only make it longer, so we can stop early for that start index.

## Approach 🛠️

1. Start with the minimum answer as infinity.
2. Pick each index as a possible starting point.
3. Expand the subarray to the right while tracking the running sum.
4. When the sum becomes at least `target`, update the minimum length.
5. Break the inner loop and move to the next starting index.

## Pseudocode 🧾

```text
set minLength = infinity
set n = length of nums

for i from 0 to n - 1:
    set currentSum = 0

    for j from i to n - 1:
        currentSum += nums[j]

        if currentSum >= target:
            minLength = min(minLength, j - i + 1)
            break

if minLength is still infinity:
    return 0

return minLength
```

## Complexity 📊

- Time: `O(n^2)`
- Space: `O(1)`
