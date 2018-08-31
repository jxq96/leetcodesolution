class Solution:                                                   
    def combinationSum(self, candidates, target):                 
        """                                                       
        :type candidates: List[int]                               
        :type target: int                                         
        :rtype: List[List[int]]                                   
        """                                                       
        result = []                                               
        bag = []                                                  
        candidates.sort()                                         
        self.dfs(result, candidates, target, bag)                 
        for i in result:                                          
            i.sort()                                              
        return result                                             
                                                                  
    def dfs(self, result, candidates, target, bag):               
        sumOfBag = sum(bag)                                       
        if sumOfBag == target:                                    
            bag.sort()                                            
            if bag not in result:                                 
                result.append(bag)                                
            return                                                
        elif sumOfBag > target:                                   
            return                                                
        else:                                                     
            for i in candidates:                                  
                bag.append(i)                                     
                self.dfs(result, candidates, target, bag.copy())  
                bag.pop()  