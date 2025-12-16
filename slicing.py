name ="happy"
print(name[3])
print(name[2:5])
print(name[2:])
print(name[2:5:2])
print(name[-3])
print(name[-3:-1:1])
print(name[::3])
x = slice(2,-2)
print(name[x])

print(name[0:1] +"\n"+ name[0:2] +"\n"+ name[0:3]+"\n"+ name[0:4]+"\n"+ name[0:5])