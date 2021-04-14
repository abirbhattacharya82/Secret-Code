def encode(s):
    t=""
    if len(s)%2!=0:
        t="QQ"+s[::-1]+"QQ"
    else:
        t=s[len(s)//2:]+s[:len(s)//2]
    return t

def encode_sent(s):
    t=""
    s=s+" "
    word=""
    for i in s:
        if i!=' ' and i!=',' and i!='.' and i!='!':
            word=word+i
        else:
            t=t+encode(word)+i
            word=""
    return t
