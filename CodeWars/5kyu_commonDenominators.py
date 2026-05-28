import math

def get_lcm(a,b):
    return abs(a*b) // math.gcd(a, b)

def convert_fracts(lst):
    res = []
    # 먼저 약분해서 기약분수 만듦 : 최대공약수(GCD)로 분자 분모 나눔
    for num, den in lst:
        common = math.gcd(num, den)

        simple_num = num // common
        simple_den = den // common

        res.append([simple_num, simple_den])

    # 최소공배수(LCM)를 찾아 통일
    denominator = [item[1] for item in res]
    LCM_den = math.lcm(*denominator)

    # 분자에 곱해줌
    new_num = [[item[0] * LCM_den // item[1], LCM_den] for item in res]
    
    return new_num

# clever version

import math
from functools import reduce

def convert_fracts(lst):
    def get_lcm (a,b): # in case math.lcm is not supported
        return abs(a * b) // math.gcd(a,b)
    
    denominators = [d for _, d in lst]
    lcm_value = reduce(get_lcm, denominators)

    return [[n * (lcm_value // d), lcm_value] for n, d in lst]
