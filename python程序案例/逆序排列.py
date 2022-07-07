x=input("请输入一个正整数：")
t=len(x)
for i in range(t+1):
    print(x[t-i:t-i+1])
print("这个数总共%d位"%t)


