class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = 0
        for i in range(len(flowerbed)):
            
            left = (i-1 < 0) or (flowerbed[i-1] == 0)
            right = (i+1 == len(flowerbed)) or (flowerbed[i+1] == 0)
            
            if flowerbed[i] == 0 and left and right:
                flowerbed[i] = 1
                planted += 1 
        
        return planted >= n
