
# Add String (Easy).
# https://leetcode.com/problems/add-strings/

# sum two string (repr of an int) and return a string.



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

    def addStrings(self, num1: str, num2: str) -> str:

        # format.
        if len(num1) > len(num2):
            (num2, num1) = (num1, num2)
        num1 = num1.rjust(len(num2), '0')
        print(num1)

        if len(num1) <= 18:
            return str(int(num1) + int(num2))

        size_str_take = 18
        output = ''
        rest = 0
        while len(num1) > 0:
            num1_cut = num1[-size_str_take:]
            num2_cut = num2[-size_str_take:]
            num1 = num1[:-size_str_take]
            num2 = num2[:-size_str_take]
            sum_str = str(int(num1_cut) + int(num2_cut) + rest)
            rest = 0
            if len(sum_str) > size_str_take:
                rest = int(sum_str[0])
                sum_str = sum_str[1:]
            if len(num1) > 0 and len(sum_str) < size_str_take:
                sum_str = sum_str.rjust(size_str_take, '0')
            output = f'{sum_str}{output}'
        if rest > 0:
            output = f'{str(rest)}{output}'
        return output



    def addStr(num1: str, num2: str) -> str:
        # adition string.
        output = ''
        rest = 0
        for i in range(len(num1)-1, -1, -1):
            id1 = self.dico_num[num1[i]]
            id2 = self.dico_num[num2[i]]
            sum_digit = id1 + id2 + rest
            id_digit = sum_digit % 10
            char_digit = next([ k for k, v in self.dico_num.items() if v == id_digit ].__iter__(), None)
            rest = sum_digit // 10
            output = f'{char_digit}{output}'
        if rest > 0:
            output = f'{rest}{output}'
        return output


