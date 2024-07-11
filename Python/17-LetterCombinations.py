class Solution(object):
    
    def backtracking(self,output, combi, remaining_digits, number_letter_mapping):
        if not remaining_digits:
            output.append(combi)
        else:
            for letter in number_letter_mapping[remaining_digits[0]]:
                self.backtracking(output, combi + letter, remaining_digits[1:], number_letter_mapping)
                
            return output
                
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if not digits: return []
        
        number_letter_mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        return self.backtracking([],"", digits, number_letter_mapping)