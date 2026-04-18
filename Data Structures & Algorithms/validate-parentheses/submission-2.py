class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closeToOpen = {
            ')':'(',
            ']':'[',
            '}':'{',
        }

        for br in s:
            if br in closeToOpen:
                if stack and stack[-1] == closeToOpen[br]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(br)
                
            
        return True if not stack else False

        