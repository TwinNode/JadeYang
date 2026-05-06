"""
solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
"""

def solution(chars):
    read = 0
    output = []

    while read < len(chars):
        start = read

        while read + 1 < len(chars) and chars[read+1] == chars[read] + 1:
            read += 1

        end = read
        count = end - start + 1

        if (count >= 3):
            output.append(str(chars[start])+"-"+str(chars[end]))
        elif (count ==2):
            output.append(str(chars[start]))
            output.append(str(chars[end]))
        else:
            output.append(str(chars[start]))

        read += 1

    print(output)
    return ",".join(output)
    

args = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
solution(args)
