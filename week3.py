def ascending(l):
    for i in range(0,len(l)-1):
        if l[i]>l[i+1]:
            return False
    return True
def alternating(l):
    for i in range(0,len(l)-2):
        if l[i]>l[i+1] and l[i+1]>=l[i+2]:
            return False
        elif l[i]<l[i+1] and l[i+1]<=l[i+2] :
            return False
    return True
def matmult(m1,m2):
    d=[]
    for i in range(0,len(m1)):
        c=[]
        for j in range(0,len(m2[0])):
            l=0
            for k in range(0,len(m2)):
                l += m1[i][k] * m2[k][j]
            c.append(l)
        d.append(c)
    return d
