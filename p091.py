0<= x1, y1, x2, y2 <= t

|\
| \
|  \
|   \
|    \
|_____\

Case 1: right angle on origin, t*t solutions
Case 2: right angle on axis, 2 axis, 2*t*t
Case 3: right angle somewhere in middle, point (a,b) where gcd(a, b) = 1
        REMEMBER TO MULTIPLY BY 2 FOR REFLECTED CASE, BUT NOT FOR CASE 1,1
        and 0<a<b<some limit and a+b<=t
        slope of one leg = b/a, other is -a/b
        now consider scaled legs, O to r has position (n*a, n*b)
        n,m>0
        other vertex has position:
            (n*a + m*b, n*b - m*a) 
            n*a + m*b <= t and n*b >= m*a
            m <= n*b/a
            Range of tests
            0 < n <= t*a/(a**2+b**2)
            0 < m <= t*b/(a**2+b**2)
        or
            (n*a - m*b, n*b + m*a)
            n*b + m*a <= t and n*a >= m*b
            m <= n*a/b
            Range of tests
            0 < n <= t*b/(a**2+b**2)
            0 < m <= t*a/(a**2+b**2)
