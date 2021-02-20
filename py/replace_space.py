class Solution1:
    def replaceSpace(self, s: str) -> str:
        res = []
        for c in s:
            if c == ' ': res.append("%20")
            else: res.append(c)
        return "".join(res)

class Solution2:
    def replaceSpace(self, s: str)-> str:
        return s.replace(" ", "%20")


class Solution3:
    def replaceSpace(self, s: str) -> str:
        s = s.split(' ')
        return "%20".join(s)