"""🧭 This file collects multiple approaches for solving the Minimum Size
Subarray Sum problem. Each method represents a different strategy, so the
main `Solution` class can choose the one it wants to run."""

from typing import List
from bisect import bisect_left

class Approaches:
    
    def _approach_1_Brute_Force(self) -> int:
        # 🏁 Start with "infinity" so any real valid window becomes the new best answer.
        min_SubArray_Length = float('inf')

        # 📏 Cache the array length once so we do not recompute it in every loop.
        n: int = len(self._nums)
        
        # 🚶 Try every possible starting index for a subarray.
        for i in range(n):
            # 🧮 Reset the running sum for the new starting position.
            current_SubArray_Sum: int = 0

            # 🔍 Expand the subarray one element at a time from index `i`.
            for j in range(i, n):
                current_SubArray_Sum += self._nums[j]

                # ✅ The moment we reach the target, check if this window is the shortest so far.
                if current_SubArray_Sum >= self._target:
                    min_SubArray_Length = min(
                        min_SubArray_Length, 
                        j - i + 1
                    )

                    # ✂️ No need to keep expanding this window, because it would only get longer.
                    break

        # 🎯 If we found at least one valid window, return its minimum length.
        # Otherwise, return 0 to show that no qualifying subarray exists.
        return (
            min_SubArray_Length 
            if min_SubArray_Length != float('inf') 
            else 0
        )
    
    def _approach_2_Sliding_Window(self) -> int:
        # 🏁 Start with "infinity" so the first valid window can set the shortest length.
        min_SubArray_Length = float('inf')

        # 🧮 Track the sum of the current window and its left/right boundaries.
        current_SubArray_Sum: int = 0
        left_Pointer: int = 0
        right_Pointer: int = 0

        # 📏 Save the array length once so the loop condition stays simple.
        n: int = len(self._nums)

        # 🚪 Expand the window by moving the right pointer across the array.
        while right_Pointer < n:
            # ➕ Include the new right-side element in the running window sum.
            current_SubArray_Sum += self._nums[right_Pointer]

            # ✅ Once the window reaches the target, keep shrinking it from the left
            # to squeeze out the smallest valid window ending at `right_Pointer`.
            while current_SubArray_Sum >= self._target:
                min_SubArray_Length = min(
                    min_SubArray_Length,
                    right_Pointer - left_Pointer + 1
                )

                # ✂️ Remove the leftmost value and move `left_Pointer` forward
                # so we can test a tighter window.
                current_SubArray_Sum -= self._nums[left_Pointer]
                left_Pointer += 1
            
            # 👉 Move right to explore the next possible window.
            right_Pointer += 1

        # 🎯 Return the best window length we found, or 0 if no valid window exists.
        return (
            min_SubArray_Length
            if min_SubArray_Length != float('inf')
            else 0
        )
    
    def _approach_3_Prefix_Sum_Binary_Search(self) -> int:
        # 🏁 Start with "infinity" so the first valid subarray can set the answer.
        min_SubArray_Length = float('inf')

        # 📏 Store the array length and prepare a prefix sum array of size `n + 1`.
        # `prefix_Sum[i]` will hold the sum of the first `i` elements.
        n: int = len(self._nums)
        prefix_Sum: List[int] = [0] * (n + 1)

        # 🧮 Build the prefix sum array so subarray sums can be reasoned about quickly.
        for current_Index in range(n):
            prefix_Sum[current_Index + 1] = (
                prefix_Sum[current_Index] + self._nums[current_Index]
            )
        
        # 🔍 Treat each index as the start of a subarray.
        for current_Index in range(n):
            # 🎯 We want the earliest prefix sum that is at least
            # `current prefix + target`, because that means the subarray sum
            # from `current_Index` to that position reaches the target.
            target_Prefix_Sum: int = (
                self._target + prefix_Sum[current_Index]
            )
            
            # 📌 `bisect_left` finds the leftmost index where `target_Prefix_Sum`
            # can be inserted while keeping the prefix sums sorted.
            target_Index: int = bisect_left(prefix_Sum, target_Prefix_Sum)
            
            # ✅ If the found index stays inside bounds, we found a valid subarray.
            if target_Index <= n:
                min_SubArray_Length = min(
                    min_SubArray_Length,
                    target_Index - current_Index
                )

        # 🎯 Return the shortest valid length, or 0 if no such subarray exists.
        return (
            min_SubArray_Length
            if min_SubArray_Length != float('inf')
            else 0
        )
