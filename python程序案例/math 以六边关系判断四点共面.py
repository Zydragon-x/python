print("请输入六边a,b,c,t,u,v.其中a与t，b与u，c与v是三对没有公共端点的线段")

a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
t=float(input("t="))
u=float(input("u="))
v=float(input("v="))

F=a*a*t*t*(-a*a-t*t+b*b+u*u+c*c+v*v)+b*b*u*u*(a*a+t*t-b*b-u*u+c*c+v*v)+c*c*v*v*(a*a+t*t+b*b+u*u-c*c-v*v)-(a*a*b*b*c*c+a*a*u*u*v*v+b*b*t*t*v*v+c*c*t*t*u*u)

print("F(a,b,c,t,u,v)=%d"%F)

if F==0:
   print("四点共面")
elif F>0:
   print("四点不共面")
   V=F/144
   print("其构成的四面体体积的平方为%f"%V)
else:
    print("四点不存在")



   
