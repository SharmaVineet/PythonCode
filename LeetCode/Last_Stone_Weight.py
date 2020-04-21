class Solution:
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            max1 = max(stones)
            stones.remove(max1)
            max2 = max(stones)
            stones.remove(max2)
            if max1 != max2:
                stones.append(abs(max1 - max2))
            elif max1 == max2 and len(stones) == 0:
                return 0
        return stones[0]


s = Solution()
print(s.lastStoneWeight([2, 2]))
