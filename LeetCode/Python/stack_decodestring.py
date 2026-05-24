class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        now_str = ""
        now_num = 0

        for x in s:
            if x.isnumeric():
                now_num = now_num * 10 + int(x)
            
            if x.isalpha():
                now_str += x
                print(now_str)

            if x == "[":
                stack.append((now_num, now_str))
                now_num = 0
                now_str = ""

            if x == "]":
                prev_num, prev_str = stack.pop()
                now_str = prev_str + (now_str * prev_num)

        return now_str
