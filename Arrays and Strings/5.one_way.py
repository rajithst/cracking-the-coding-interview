class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        n1 = len(s)
        n2 = len(t)

        # always,get n1 as short string
        if n1 > n2:
            return self.isOneEditDistance(t, s)
        # if lengths difference is greater than 1,return False
        if n2 - n1 > 1:
            return False

        for i in range(n1):
            # if we found a mismatch,compare rest of the string
            if s[i] != t[i]:
                # if both lengths are equal,we can't insert/delete a character,only we can replace
                # if we replace current character,
                # rest of the strings should equal
                if n1 == n2:
                    return s[i + 1:] == t[i + 1:]
                else:
                    # if we can insert a character
                    return s[i:] == t[i + 1:]

        # if we did not find a mismatch,we can delete character
        return n1 + 1 == n2
