class Solution:
    def calculate(self, s: str) -> int:
        return self.parse_expr(s, 0)[0]

    def parse_expr(self, s, i):
        stack = []
        num = 0
        sign = '+'
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == '(':
                num, i = self.parse_expr(s, i + 1)
            if (not s[i].isdigit() and s[i] != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                num = 0
                sign = s[i]
            if s[i] == ')':
                return sum(stack), i
            i += 1
        return sum(stack), i