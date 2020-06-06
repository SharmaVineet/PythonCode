class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        for i in numbers:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1


s = Solution()
print(s.twoSum([2, 5, 7, 11, 13], 18))
