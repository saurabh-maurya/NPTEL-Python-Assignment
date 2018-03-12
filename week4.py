def histogram(l):
    c=[]
    while len(l) :
        a=l[0]
        count=0
        for i in range(0,len(l)) :
            if a==l[i]:
                count=count+1
        while a in l :
            l.remove(a)
        c.append((a,count))
    c=sorted(c)
    c=sorted(c,key=lambda c:c[1])
    return c
def transcript(coursedetails,studentdetails,grades):
    m=[]
    studentdetails=sorted(studentdetails)
    for i in range(0,len(studentdetails)) :
        l=[]
        for j in range(0,len(grades)) :
            if studentdetails[i][0]==grades[j][0] :
                for k in range(0,len(coursedetails)) :
                    if grades[j][1]==coursedetails[k][0] :
                        x=(coursedetails[k][0],coursedetails[k][1],grades[j][2])
                l.append(x)
            l=sorted(l)
            y=(studentdetails[i][0],studentdetails[i][1],l)
        m.append(y)
    return(m)


print(histogram([13,12,11,13,14,13,7,7,13,14,12]))
print((transcript([("MA101","Calculus"),("PH101","Mechanics"),("HU101","English")],[("UGM2018001","Rohit Grewal"),("UGP2018132","Neha Talwar")],[("UGM2018001","MA101","AB"),("UGP2018132","PH101","B"),("UGM2018001","PH101","B")])))
