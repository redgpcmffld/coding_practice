# Given two binary strings a and b, return their sum as a binary string.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        final_result = ''
        locations = {}
        num_list = []

        def Binary(str):
            result = 0
            length = len(str) - 1
            for i in str:
                result += int(i) * (2 ** length)
                length -= 1
            return result
        number = Binary(a) + Binary(b)
        j = 0
        while number // 2 != 0:
            locations[j] = number % 2
            num_list.append(str(locations[j]))
            number = int(number // 2)
            j += 1
        num_list.append(str(number))
        for n in num_list:
            final_result += n
        return final_result[::-1]
