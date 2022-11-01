class Solution:
    def isAnagram(self, firstArray: str, secondArray: str) -> bool:
        
    # O(firstArrayCout + secondArrayCount) time | O(firstArrayCout + secondArrayCount) space
    # O(s + t) time | O(s + t) space

        if len(firstArray) != len(secondArray):
            return False
        
        firstArrayCount = {}
        secondArrayCount = {}
        
        for idx in range(len(firstArray)):
            firstArrayCount[firstArray[idx]] = 1 + firstArrayCount.get(firstArray[idx], 0)
            secondArrayCount[secondArray[idx]] = 1 +secondArrayCount.get(secondArray[idx],0)
        for character in firstArrayCount:
            if firstArrayCount[character] != secondArrayCount.get(character, 0):
                return False
            
        return True
            
            
            
                           
        
        