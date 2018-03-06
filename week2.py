def sumofsquares(m) :
    I = 1
    while I * I <= m :
        K = 1
        while(K * K <= m) :
            if (I * I + K * K == m) :
                return True
            K = K + 1
        I = I + 1

    return False

def wellbracketed(s):
    start_bracket = 0
    end_bracket = 0
    for i in range(0,len(s)):
        if ( s[i] == "(" ) :
            start_bracket = start_bracket + 1
        elif ( s[i] == ")" ) :
            end_bracket = end_bracket + 1
        else:
            continue
    if end_bracket == start_bracket:
        return True
    else:
        return False

def rotatelist(l,k):
    for j in range(0,k):
        c =[]
        c.append(l[-1])
        for i in range(0,len(l)-1):
            c.append(l[i])
        l=c
    return c
