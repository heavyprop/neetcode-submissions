class Solution:
    def isValid(self, s: str) -> bool:
        check = {
            "{" : "}",
            "[" : "]",
            "(" : ")",
        }
        stack = []
        for item in s:
            if item in check.keys():
                stack.append(item)
            if item in check.values():
                if not stack:
                    return False
                else:
                    key = stack.pop()
                #if check.keys(key) != check.value(item):
                if check.get(key) != item:
                        return False
        
        if stack:
            return False
        return True
