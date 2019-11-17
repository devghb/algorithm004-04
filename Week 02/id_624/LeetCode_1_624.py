#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (46.74%)
# Likes:    6549
# Dislikes: 0
# Total Accepted:    603.6K
# Total Submissions: 1.3M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
# 
# 示例:
# 
# 给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 
# 
#

# @lc code=start
class Solution:
    # 使用hashSet的最优解法
    def twoSum(self, nums: [int], target: int) -> [int]:
        dict = {}
        for i, n in enumerate(nums):
            if target - n in dict:
                return [dict[target-n], i]
            dict[n] = i
        
# @lc code=end

