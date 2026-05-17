"""
You know what divisors of a number are. The divisors of a positive integer n are said to be proper when you consider only the divisors other than n itself. 
In the following description, divisors will mean proper divisors. For example for 100 they are 1, 2, 4, 5, 10, 20, 25, and 50.

Let s(n) be the sum of these proper divisors of n. Call buddy two positive integers such that the sum of the proper divisors of each number is one more than the other number:

(n, m) are a pair of buddy if s(m) = n + 1 and s(n) = m + 1

Task
Given two positive integers start and limit, the function buddy(start, limit) should return the first pair (n m) of buddy pairs such that n (positive integer) is between start (inclusive) and limit (inclusive); 
m can be greater than limit and 
⚠ has to be greater than n

"""
def buddy(start, limit):
    for n in range(start, limit + 1):
        m = s(n) - 1  
        
        if m > n and s(m) - 1 == n:
            return [n, m]
            
    return "Nothing"
  
def s(n):
    total = 1  # 1은 모든 수의 약수이므로 미리 더해둡니다.
    
    # n**0.5(중간지점)까지 돌면서 작은 약수(i)와 큰 약수(n//i)를 세트로 더함
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i * i != n:  # 제곱근 중복 방지 (예: 6*6=36일 때 6을 두번 더하지 않게)
                total += n // i
    return total
