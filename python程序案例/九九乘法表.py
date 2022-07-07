t=0
for i in range(1,10):
    for t in range(1,10):
        print("{}*{}={}\t".format(i,t,i*t),end="")
    print()
print()



t=0
for a in range(1,10):
    for b in range(1,11-a):
        print("{}*{}={}\t".format(a,b,a*b),end="")
    print()
print()


t=0
for u in range(1,10):
    for v in range(1,u+1):
        print("{}*{}={}\t".format(u,v,u*v),end="")
    print()
print()

