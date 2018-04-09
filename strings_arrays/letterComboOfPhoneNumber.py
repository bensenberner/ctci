dig = {
    "2": set("abc"),
    "3": set("def"),
    "4": set("ghi"),
    "5": set("jkl"),
    "6": set("mno"),
    "7": set("pqrs"),
    "8": set("tuv"),
    "9": set("wxyz")
}

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        if not digits: return [""]
        curr_digit = digits[0]
        for letter in dig[curr_digit]:
            print(letter)
            res.extend([letter + word for word in self.letterCombinations(digits[1:])])
        return res

s = Solution()
print(s.letterCombinations("23"))
