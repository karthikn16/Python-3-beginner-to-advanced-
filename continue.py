abc = "A,B,F,D,W,R,T"
asd =''

for i in abc:
    if i ==',':
        continue
    asd = asd + i

print(asd)