import random
def number_right(a,b):
    if a<b:
        print("猜小了!")
        return False
    elif a>b:
        print("猜大了!")
        return False
    else:
        print("猜对了!")



def main():
    b=random.randint(1,1001)
    fg=False
    x=0
    while fg==False:
        a=int(input("请猜一个1到1000之间的数："))
        fg=number_right(a,b)
        x=x+1
    print("总共猜了%d次"%x)

if __name__=='__main__':
    main()
