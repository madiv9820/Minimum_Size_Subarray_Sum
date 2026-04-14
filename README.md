# Minimum Size Subarray Sum 🚀

You are given:
- an array of **positive integers** `nums`
- a **positive integer** `target`

Your task is to find the **smallest length** of a **contiguous subarray** whose sum is **greater than or equal to** `target`.

If no such subarray exists, return **`0`**.

### What is a subarray? 📚

A subarray is a **continuous part** of the array.

For example, in `[2,3,1,2,4,3]`, these are valid subarrays:
- `[2,3]`
- `[3,1,2]`
- `[4,3]`

But `[2,1,4]` is **not** a subarray because the elements are not contiguous.

### Examples 💡

#### Example 1
**Input:** `target = 7`, `nums = [2,3,1,2,4,3]`  
**Output:** `2`

**Explanation:**  
The subarray `[4,3]` has sum `7`, so the minimum length is **2** ✅

#### Example 2
**Input:** `target = 4`, `nums = [1,4,4]`  
**Output:** `1`

**Explanation:**  
The subarray `[4]` already meets the target, so the answer is **1** 🎯

#### Example 3
**Input:** `target = 11`, `nums = [1,1,1,1,1,1,1,1]`  
**Output:** `0`

**Explanation:**  
Even the sum of the whole array is only `8`, which is less than `11`, so no valid subarray exists ❌

### Constraints 📏

- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

### In Short 🧠

Find the **shortest continuous chunk** of the array whose sum is at least `target`.

## Approach Pages 📚

- [**Brute Force 🐢**](./docs/brute-force.md)
- [**Sliding Window 🚪**](./docs/sliding-window.md)
- [**Prefix Sum + Binary Search 🔍**](./docs/prefix-sum-binary-search.md)