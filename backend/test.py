from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, k in enumerate(flowerbed):
            if k == 0:
                prev = flowerbed[i - 1] if i > 0 else 0
                next_ = flowerbed[i + 1] if i < len(flowerbed) - 1 else 0
                if prev == 0 and next_ == 0:
                    n -= 1
                    flowerbed[i] = 1
            if n <= 0:
                        return True
            
              
        return False

ans = Solution().canPlaceFlowers(flowerbed=[0,0,0,0,0,1,0,0], n = 0)
print(ans)  # Output: True
