a=float(input())
b=float(input())
c=float(input())
d=float(input())

import math
ans1=(a*math.log2(a)+b*math.log2(b))*(-1)
ans2=(c*math.log2(c)+d*math.log2(d))*(-1)

print(ans1)
print(ans2)
#print(ans3)
total=0.971
e=float(input())
f=float(input())
#g=float(input())
total-=e*ans1
total-=f*ans2
#otal-=g*ans3
print(total)



"""a=float(input())
b=float(input())
c=float(input())
d=float(input())
import math
ans1=(a*math.log2(a)+b*math.log2(b))*(-1)
ans2=(c*math.log2(c)+d*math.log2(d))*(-1)
print(ans1)
print(ans2)
total=0.940
e=float(input())
f=float(input())

total-=e*ans1
total-=f*ans2
print(total)
"""