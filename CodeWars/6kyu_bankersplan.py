def fortune(f0, p, c0, n, i):
    for x in range(n-1):

        f0 = int(f0 + (0.01*p*f0) - c0)
        c0 += int(c0*0.01*i)
        
    return f0 >= 0 
