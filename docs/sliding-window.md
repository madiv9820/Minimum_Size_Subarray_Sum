# Sliding Window 🚪

[⬅ Back to README](../README.md)

### Intuition 💡

Since every number in `nums` is **positive**, the **window sum** changes in a predictable way:
- adding an element on the right **increases** the sum
- removing an element from the left **decreases** the sum

That lets us maintain a **moving window** instead of restarting from scratch every time.
We **expand** until the sum is large enough, then **shrink** from the left to find the shortest valid window.

### Approach 🛠️

1. Use two pointers, `left` and `right`, to represent the **current window**.
2. Move `right` forward and add each new value into the **running sum**.
3. Once the sum is at least `target`, update the **answer**.
4. Keep shrinking from the left while the window still stays **valid**.
5. Continue until the right pointer reaches the end.

### Pseudocode 🧾

```text
set minLength = infinity
set currentSum = 0
set left = 0

for right from 0 to n - 1:
    currentSum += nums[right]

    while currentSum >= target:
        minLength = min(minLength, right - left + 1)
        currentSum -= nums[left]
        left += 1

if minLength is still infinity:
    return 0

return minLength
```

### Complexity 📊

- **Time:** `O(n)` <br>
  Each element is added to the window once and removed at most once, so the two pointers move linearly.

- **Space:** `O(1)`<br>
  The algorithm uses only a few variables besides the input array.
