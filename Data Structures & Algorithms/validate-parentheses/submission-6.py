class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        for char in s:
            if char == "(":
                stack.append(")")
            elif char == "{":
                stack.append("}")
            elif char == "[":
                stack.append("]")
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if char != popped:
                    return False
        if(len(stack) > 0):return False
        return True
