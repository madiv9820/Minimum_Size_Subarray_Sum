# Prefix Sum + Binary Search 🔍

[⬅ Back to README](../README.md)

### Intuition 💡

**Prefix sums** let us express any subarray sum quickly.

If `prefix[i]` is the **sum of the first `i` elements**, then the sum from index `i` to `j - 1` is:

`prefix[j] - prefix[i]`

For every **starting index** `i`, we want the **smallest** `j` such that:

`prefix[j] - prefix[i] >= target`

That becomes:

`prefix[j] >= prefix[i] + target`

Now we just need to find the **earliest prefix sum** that is large enough. Since prefix sums are **sorted** when all numbers are positive, **binary search** works neatly here.

### Approach 🛠️

1. Build a **prefix sum array** of length `n + 1`.
2. For each starting index, compute the required **prefix sum threshold**.
3. Use **binary search** to find the first prefix sum that is at least that threshold.
4. If such an index exists, update the **minimum subarray length**.

### Pseudocode 🧾

```text
set minLength = infinity
set n = length of nums
create prefixSum array of size n + 1 filled with 0

for i from 0 to n - 1:
    prefixSum[i + 1] = prefixSum[i] + nums[i]

for i from 0 to n - 1:
    needed = prefixSum[i] + target
    j = lower_bound(prefixSum, needed)

    if j <= n:
        minLength = min(minLength, j - i)

if minLength is still infinity:
    return 0

return minLength
```

### Complexity 📊

- **Time:** `O(n log n)` <br>
  We iterate through the array once, and for each index we perform a binary search on the prefix sum array.

- **Space:** `O(n)` <br>
  The extra prefix sum array stores `n + 1` values, so the memory grows linearly with the input size.
