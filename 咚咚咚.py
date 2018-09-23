print([a for a in range(5)])
ls=[x for x in  range(5)]
q=[]
w=[lambda x:a+x for a in range(5)]
for x in w:
    print(x(1))

for a in range(5):
    q.append(lambda x:a+x)

print(q[0](1),q[1](1),q[2](1))
