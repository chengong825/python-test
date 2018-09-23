x=int(input())
y=int(input())
z=int(input())
if x>y:
    t=x
    x=y
    y=t
if x>z:
    t=x
    x=z
    z=t
if y>z:
    t=y
    y=z
    z=t
print(x,y,z)