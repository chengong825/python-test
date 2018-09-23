import random
n=random.randint(0,99)
i=1
while i<=20:
    s=int(input("猜一个数"))
    if s==n:
        break
    elif s>n:
        print("大了")
    elif s<n:
        print("小了")
    i+=1
if i==1 or i==2:
    print("你太TM有才了！")
elif 3<=i<=6:
    print("这么快就猜出来了，很聪明嘛！")
elif 7<=i<=20:
    print("猜了半天才猜出来，小同志，尚需努力啊!")
else:
    print("gg")