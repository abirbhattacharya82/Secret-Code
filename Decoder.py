def decode(s):
    t=""
    if len(s)%2==0:
        t=s[len(s)//2:]+s[:len(s)//2]
    else:
        t=s[2:len(s)-2]
        t=t[::-1]
    return t

def decode_sent(s):
    t=""
    s=s+" "
    word=""
    for i in s:
        if i!=' ' and i!=',' and i!='.' and i!='!':
            word=word+i
        else:
            t=t+decode(word)+i
            word=""
    return t
