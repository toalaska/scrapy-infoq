# coding=utf-8
arr=[]
r=160
g=160
for b in range(160):
    one= '''<div style="height:20px;width:100px;background:rgb(%s,%s,%s)"></div>''' % (r,g,b)
    arr.append(one)

with open("color.html","w") as f:
    f.write("\n".join(arr))

