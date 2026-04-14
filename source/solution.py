"""🧭 This file exposes the final `Solution` class used by the tests or
online judge. It receives the input, stores shared state, and delegates
the actual work to one of the inherited solving approaches."""

from typing import List
from source.approaches import Approaches

class Solution(Approaches):
    # 🧩 `Solution` inherits the different solving strategies from `Approaches`
    # and chooses which one to run for the final answer.
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 📥 Store the input on the instance so the inherited approach methods
        # can use the same shared data without passing it around repeatedly.
        self._target = target
        self._nums = nums
        
        # 🚀 Pick the approach we want to use for this submission.
        # return self._approach_1_Brute_Force
        # return self._approach_2_Sliding_Window
        # return self._approach_3_Prefix_Sum_Binary_Search()