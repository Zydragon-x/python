def jc(n):
    if n<0:return("输入错误")
    if n==0:return 1
    else:return n*jc(n-1)
