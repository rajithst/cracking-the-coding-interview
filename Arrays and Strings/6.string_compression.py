from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        i = 0
        k = 0
        while i < len(chars):
            # iterate while current letter is equal to previous letter
            # (find the start and end of the group)
            j = i
            while j < len(chars) and chars[i] == chars[j]:
                j += 1

            # keep copy of result letter
            chars[k] = chars[i]
            # increase k by 1 to get the insert position of count
            k += 1

            # if group size is greater than 1,need to add group size
            if j - i > 1:
                # if group size is greater than 10,fill each digit
                s = str(j - i)
                for c in s:
                    chars[k] = c
                    k += 1
            i = j

        return k

