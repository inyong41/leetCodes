class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _max = 0
        head = 0
        for index, char in enumerate(s):
            for i in range(head, index):
                if char == s[i]:
                    head = i + 1
                    break
            _len = index - head + 1
            _max = _max if _max > _len else _len
        return _max