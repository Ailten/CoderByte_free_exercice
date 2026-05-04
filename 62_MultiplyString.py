
# Multiply String (Easy).
# https://leetcode.com/problems/multiply-strings/

# multiply two string (repr of int) and return the result in string format. (avoid cast or library).


class Solution:
    dico_num = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }

    def multiply(self, num1: str, num2: str) -> str:
        
        # easily solution. (but include cast int).
        i1 = int(num1)
        i2 = int(num2)
        return str(i1 * i2)

        # cast re-write.
        #i1 = self.castStrToInt(num1)
        #i2 = self.castStrToInt(num2)
        #output = self.castIntToStr(i1 * i2)
        #return output if len(output) > 0 else '0'

    def castStrToInt(self, str_num: str) -> int:
        output = 0
        for char in str_num:
            digit = Solution.dico_num.get(char, None)
            if digit == None:
                raise Exception('not a number cast')
            output = (output * 10) + digit
        return output
    
    def castIntToStr(self, int_num: int) -> str:
        output = ''
        while int_num > 0:
            digit = int_num % 10
            int_num //= 10
            char = next([ k for k, v in Solution.dico_num.items() if v == digit ].__iter__(), None)
            if char == None:
                raise Exception('not a number cast')
            output = f'{char}{output}'
        return output
    