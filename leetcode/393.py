from typing import List


# class Solution:
#     def validUtf8(self, data: List[int]) -> bool:
#         utf8_list = []
#         data_length = len(data)
#         i = 0
#         for n in data:
#             utf8_list.append(bin(n)[2:].zfill(8))
#         while i < data_length:
#             if utf8_list[i].startswith('0'):
#                 pass
#             elif utf8_list[i].startswith('110') and i + 1 < data_length:
#                 for _ in range(1):
#                     i += 1
#                     if not utf8_list[i].startswith('10'):
#                         return False
#             elif utf8_list[i].startswith('1110') and i + 2 < data_length:
#                 for _ in range(2):
#                     i += 1
#                     if not utf8_list[i].startswith('10'):
#                         return False
#             elif utf8_list[i].startswith('11110'):
#                 for _ in range(3):
#                     i += 1
#                     if not utf8_list[i].startswith('10') and i + 3 < data_length:
#                         return False
#             else:
#                 return False
#             i += 1
#         return True

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        if not data:
            return False
        data_length = len(data)
        i = 0
        while i < data_length:
            num = 0
            if data[i] & 0b10000000 == 0:
                num = 1
            elif data[i] & 0b11100000 == 0b11000000:
                num = 2
            elif data[i] & 0b11110000 == 0b11100000:
                num = 3
            elif data[i] & 0b11111000 == 0b11110000:
                num = 4
            else:
                return False
            for j in range(1, num):
                if i + j >= data_length or data[i + j] & 0b11000000 != 0b10000000:
                    return False
            i = i + num

        return True



if __name__ == "__main__":
    data = [237]
    ret = Solution()
    print(ret.validUtf8(data))

"""
startwith함수를 이용하여 풀었지만 비트조작을 이용한 풀이가 더 빨라서 비트조작으로 다시 풀어보았다.
"""