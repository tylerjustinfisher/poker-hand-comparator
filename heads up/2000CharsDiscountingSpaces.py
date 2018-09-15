def n(u,v):
    if u[5]!=v[5]: return u[5]>v[5]
    if u[5]==8 or u[5]==4: return u[2]>v[2] if u[2]!=v[2] else None
    if u[5]==5 or u[5]==0:
        for w in range(5):
            if u[4-w]!=v[4-w]: return u[4-w]>v[4-w]
        return None
    for g in range(6,10):
        if u[g]!=v[g]: return u[g]>v[g]
        if len(u)==g+1: return None
def o(e,t):
    y=None
    for i in range(7):
        for j in range(i+1, 7):
            s=[]
            for k in range(7):
                if k!=i and k!=j: s.extend([e[k],t[k]])
            b=p(sorted([s[0],s[2],s[4],s[6],s[8]]), [s[1],s[3],s[5],s[7],s[9]])
            if y is None or n(b,y): y=b
    return y
def p(z,l):
    if l.count(l[0])==len(l): z.append(8) if ((z[0]==z[1]-1==z[2]-2==z[3]-3) and (z[4]-1==z[3] or z[4]-12==z[0])) else z.append(5)
    elif ((z[0]==z[1]-1==z[2]-2==z[3]-3) and (z[4]-1==z[3] or z[4]-12==z[0])): z.append(4)
    elif z[1]==z[2]==z[3] and (z[0]==z[1] or z[3]==z[4]): z.extend([7,z[0],z[4]]) if z[0]==z[1] else z.extend([7,z[4],z[0]])
    elif z[0]==z[1]==z[2] and z[3]==z[4]: z.extend([6,z[0],z[4]])
    elif z[0]==z[1] and z[2]==z[3]==z[4]: z.extend([6,z[4],z[0]])
    elif z[0]==z[1]==z[2]: z.extend([3,z[0],z[4],z[3]])
    elif z[2]==z[3] and (z[1]==z[2] or z[3]==z[4]): z.extend([3,z[1],z[4],z[0]]) if z[1]==z[2] else z.extend([3,z[2],z[1],z[0]])
    elif (z[0]==z[1] and (z[2]==z[3] or z[3]==z[4])) or (z[1]==z[2] and z[3]==z[4]):
        if z[0]==z[1] and z[2]==z[3]: z.extend([2, z[3], z[1], z[4]])
        else: z.extend([2,z[4],z[1],z[2]]) if z[0]==z[1] and z[3]==z[4] else z.extend([2,z[4],z[1],z[0]])
    elif z[0]==z[1] or z[1]==z[2]: z.extend([1, z[0],z[4],z[3],z[2]]) if z[0]==z[1] else z.extend([1,z[1],z[4],z[3],z[0]])
    elif z[2]==z[3] or z[3]==z[4]: z.extend([1, z[2],z[4],z[1],z[0]]) if z[2]==z[3] else z.extend([1,z[3],z[2],z[1],z[0]])
    return z if len(z)>5 else z+[0]
c,a=[ int(r) for r in ((",".join(str(ord(e)) for e in (raw_input(">:").replace("T",":").replace("J",";").replace("Q","<").replace("K","=").replace("A",">")))).split(',')) ], ["highCard","pair","2pair","trips","straight","flush","boat","quads","SF"]
d,f=o([c[0],c[2],c[10],c[12],c[14],c[16],c[18]],[c[1],c[3],c[11],c[13],c[15],c[17],c[19]]),o([c[5],c[7],c[10],c[12],c[14],c[16],c[18]],[c[6],c[8],c[11],c[13],c[15],c[17],c[19]])
print("TIE, " + a[d[5]] if n(d,f) is None else '%s wins, ' % (1 if n(d,f) else 2) + (a[d[5]] if n(d,f) else a[f[5]]))
