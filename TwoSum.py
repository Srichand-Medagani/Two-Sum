**Two sum**

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Example:**

Given nums = [2, 7, 11, 15], target = 9,  

Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
"""

l=list(map(int,input().split()))
t=input()
q=[]
m=[]
for i in range(0,len(l)):
    p=[]
    c=0
    b=0
    for j in range(1,len(l)):
        if i!=j:
            c=int(l[i])
            b=int(l[j])
            if c+b==t:
                p.append(c)
                p.append(b)
                p.sort()
                if not p in q:
                    q.append(p)
for i in range(0,len(q)):
    for j in range(1,len(q)):
        if i!=j and i<j:
            m.append(q[i]+q[j])
    m[i].sort()
print(m)
